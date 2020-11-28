import datetime
import os
import uuid

import accounts.models
import course.models
import stream.models
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import ugettext as _
from guardian.shortcuts import assign_perm
from meta.models import ModelMeta
from notifications.signals import notify
from saiki.utils import get_site_title

from .utils import file_cleanup

""" Whenever ANY model is deleted, if it has a file field on it, delete the associated file too"""
@receiver(post_delete)
def delete_files_when_row_deleted_from_db(sender, instance, **kwargs):
    for field in sender._meta.concrete_fields:
        if isinstance(field,models.FileField):
            instance_file_field = getattr(instance,field.name)
            delete_file_if_unused(sender,instance,field,instance_file_field)

""" Delete the file if something else get uploaded in its place"""
@receiver(pre_save)
def delete_files_when_file_changed(sender,instance, **kwargs):
    # Don't run on initial save
    if not instance.pk:
        return
    for field in sender._meta.concrete_fields:
        if isinstance(field,models.FileField):
            #its got a file field. Let's see if it changed
            try:
                instance_in_db = sender.objects.get(pk=instance.pk)
            except sender.DoesNotExist:
                # We are probably in a transaction and the PK is just temporary
                # Don't worry about deleting attachments if they aren't actually saved yet.
                return
            instance_in_db_file_field = getattr(instance_in_db,field.name)
            instance_file_field = getattr(instance,field.name)
            if instance_in_db_file_field.name != instance_file_field.name:
                delete_file_if_unused(sender,instance,field,instance_in_db_file_field)


""" Only delete the file if no other instances of that model are using it"""    
def delete_file_if_unused(model,instance,field,instance_file_field):
    dynamic_field = {}
    dynamic_field[field.name] = instance_file_field.name
    other_refs_exist = model.objects.filter(**dynamic_field).exclude(pk=instance.pk).exists()
    if not other_refs_exist:
        instance_file_field.delete(False)

class Assignment(ModelMeta, models.Model):

    title = models.CharField(_('title'), max_length=256)
    description = models.TextField(_('description'), blank=True, null=True, max_length=256)
    deadline = models.DateTimeField(_("deadline"))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    course_offering = models.ForeignKey('course.CourseOffering', on_delete=models.CASCADE)
    slug = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    points = models.PositiveIntegerField(_("points"), default=0)

    _metadata = {
        'title': 'get_meta_assignment_title',
        'description': 'get_meta_assignment_description',
    }

    def get_meta_assignment_title(self):
        return get_site_title(f'{ self.title } - { self.course_offering.course.code }')

    def get_meta_assignment_description(self):
        return self.description[:120] + (self.description[120:] and '..')

    def __str__(self):
        return '{} - {}'.format(self.course_offering, self.title)

    def get_absolute_url(self):
        return reverse('assignment:detail', kwargs={ 'slug': self.slug })

    @property
    def is_not_in_deadline(self):
        return self.deadline < datetime.datetime.now(self.deadline.tzinfo)

def assignment_save_handler(sender, instance, created, **kwargs):
    # users who can view assignment
    users = accounts.models.User.objects.filter(student__courseenrollment__course_offered=instance.course_offering)

    # add permission to teacher, so only teacher can edit and view this assignment
    if created:
        assign_perm('add_assignment', instance.course_offering.teacher.user, instance)
        assign_perm('change_assignment', instance.course_offering.teacher.user, instance)
        assign_perm('delete_assignment', instance.course_offering.teacher.user, instance)
        assign_perm('view_assignment', instance.course_offering.teacher.user, instance)

        assign_perm('view_assignment', users, instance)

        post = stream.models.Post()
        post.stream = instance.course_offering
        post.user = instance.course_offering.teacher.user
        post.body = f'Assignment: { instance.title }'
        post.post_type = 'assignment'
        post.assignment = instance
        post.save()

        verb = 'assigned'
    else:
        verb = 'updated'
    
    description = f'{ verb } <b>{ instance.title }</b> in { instance.course_offering.course.code }'
    href = reverse('assignment:detail', kwargs={'slug': instance.slug})
    notify.send(instance.course_offering.teacher.user, verb='updated', recipient=users, action_object=instance, target=instance.course_offering, description=description, href=href)

def assignment_delete_handler(sender, instance, *args, **kwargs):
    users = accounts.models.User.objects.filter(student__courseenrollment__course_offered=instance.course_offering)
    
    description = f'deleted <b>{ instance.title }</b> in { instance.course_offering.course.code }'
    notify.send(instance.course_offering.teacher.user, verb='deleted', recipient=users, action_object=instance, target=instance.course_offering, description=description)

post_save.connect(assignment_save_handler, sender=Assignment)
post_delete.connect(assignment_delete_handler, sender=Assignment)

def upload_path(instance, filename):
    return os.path.join('assignment', str(instance.assignment.slug), filename)

class AssignmentFile(models.Model):
    file = models.FileField(upload_to=upload_path)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True, blank=True)

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension[1:]

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return '{} - {}'.format(self.assignment, self.file.name)

class AssignmentWork(models.Model):

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
    submit_date = models.DateTimeField(_("submit date"), blank=True, null=True)
    submitted = models.BooleanField(_("submitted"), default=False)
    points = models.IntegerField(_("points"), default=-1, null=True, blank=True)

    @property
    def is_submitted_on_time(self):
        return self.submit_date < self.assignment.deadline

    def __str__(self):
        return '{} - {}'.format(self.assignment, self.student)


def assignmentwork_save_handler(sender, instance, created, **kwargs):
    if created:
        assign_perm('change_assignmentwork', instance.assignment.course_offering.teacher.user, instance)
        assign_perm('view_assignmentwork', instance.assignment.course_offering.teacher.user, instance)
        
        assign_perm('change_assignmentwork', instance.student.user, instance)
        assign_perm('view_assignmentwork', instance.student.user, instance)

post_save.connect(assignmentwork_save_handler, sender=AssignmentWork)

def upload_work_path(instance, filename):
    return os.path.join('assignment' , str(instance.assignment_work.assignment.slug), 'work', str(instance.assignment_work.student.user.username), filename)

class AssignmentWorkFile(models.Model):
    file = models.FileField(upload_to=upload_work_path)
    assignment_work = models.ForeignKey(AssignmentWork, on_delete=models.CASCADE, null=True, blank=True)

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension[1:]

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return '{} - {}'.format(self.assignment_work, self.file.name)
