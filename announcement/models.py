import uuid

import accounts.models
import course.models
import university.models
from django import forms
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_delete, post_save, pre_save
from django.utils.translation import ugettext as _
from guardian.shortcuts import assign_perm, get_users_with_perms, remove_perm
from multiselectfield import MultiSelectField
from notifications.signals import notify
from textwrap import shorten

# https://stackoverflow.com/questions/4670783/make-the-user-in-a-model-default-to-the-current-user

# Create your models here.

class AnnouncementFilter(models.Model):
    title = models.CharField(_('title'), max_length=128, default='Untitled Filter')
    course = models.ManyToManyField('course.CourseOffering', blank=True, help_text="<b>Remember course and semester must not be selected at same time.</b>")
    SEMESTER_CHOICES = (
        (1, _('Semester 1')),
        (2, _('Semester 2')),
        (3, _('Semester 3')),
        (4, _('Semester 4')),
        (5, _('Semester 5')),
        (6, _('Semester 6')),
        (7, _('Semester 7')),
        (8, _('Semester 8')),
    )
    program = models.ManyToManyField('university.Program', blank=True)
    semester = models.ManyToManyField('university.Semester', blank=True)
    # semesters = MultiSelectField(_('semesters'), choices=SEMESTER_CHOICES, blank=True, null=True, help_text="<b>Remember course and semester must not be selected at same time</b>")

    def get_programs(self):
        return ", ".join([p.code for p in self.program.all()])
    get_programs.short_description = 'Programs'

    def get_courses(self):
        return ", ".join([str(p) for p in self.course.all()])
    get_courses.short_description = 'Courses Enrolled'

    def __str__(self):
        return '[{}] {}'.format(self.id, self.title)

class Announcement(models.Model):
    title = models.CharField(_('title'), max_length=128)
    description = models.TextField(_('description'), blank=True, null=True)

    created_by = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    start_date = models.DateTimeField(_('start date'))
    end_date = models.DateTimeField(_('end date'))

    # is global implies urgent
    is_global = models.BooleanField(_('is global'), default=False, help_text="If global is checked announcement filter will not work.")
    active = models.BooleanField(_('active'), default=True)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    
    slug = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    TAGS_CHOICES = (
        (1, _('University Specific')),
        (2, _('Program Specifc')),
        (3, _('Semester Specifc')),
        (4, _('Course Specifc')),
    )
    tags = MultiSelectField(_('tags'), choices=TAGS_CHOICES)

    announcement_filters = models.ForeignKey(AnnouncementFilter, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '[{}]'.format(self.id)

    class Meta:
        ordering = ['tags', '-updated_at']

    def get_absolute_url(self):
        return reverse('announcement:detail', kwargs={ 'slug': self.slug })

def announcement_save_handler(sender, instance, created, **kwargs):
    if not instance.active: return
    students = accounts.models.User.objects.filter(is_student=True)

    if not created:
        users_with_perm = get_users_with_perms(instance, only_with_perms_in=['view_announcement'])
        for user in users_with_perm:
            remove_perm('view_announcement', user, instance)

    description = f'announce <b>{ shorten(instance.title, width=40, placeholder="...") }</b>'
    href = instance.get_absolute_url()
    if instance.is_global:
        notify.send(instance.created_by, verb='announce', recipient=accounts.models.User.objects.filter(is_staff=False, is_superuser=False), action_object=instance, description=description, href=href)

    if not instance.announcement_filters: return
    
    if (instance.announcement_filters.program.filter().count() == 0 and 
        instance.announcement_filters.semester.filter().count() == 0):
        # print('course')
        users = students.filter(
            student__courseenrollment__course_offered__in=instance.announcement_filters.course.filter()
        )
    elif (instance.announcement_filters.course.filter().count() == 0 and 
        instance.announcement_filters.semester.filter().count() == 0):
        # print('program')
        users = students.filter(
            student__program__in=instance.announcement_filters.program.filter()
        )
    elif (instance.announcement_filters.course.filter().count() == 0 and 
        instance.announcement_filters.program.filter().count() == 0):
        # print('semester')
        users = students.filter(
            student__semester__in=instance.announcement_filters.semester.filter()
        )
    elif (instance.announcement_filters.program.filter().count() == 0):
        # print('course + semester')
        users = students.filter(
            student__courseenrollment__course_offered__in=instance.announcement_filters.course.filter(),
            student__semester__in=instance.announcement_filters.semester.filter()
        )
    elif (instance.announcement_filters.semester.filter().count() == 0):
        # print('course + program')
        users = students.filter(
            student__courseenrollment__course_offered__in=instance.announcement_filters.course.filter(),
            student__program__in=instance.announcement_filters.program.filter()
        )
    elif (instance.announcement_filters.course.filter().count() == 0):
        # print('program + semester')
        users = students.filter(
            student__program__in=instance.announcement_filters.program.filter(),
            student__semester__in=instance.announcement_filters.semester.filter()
        )
    else:
        # print('course + semester + program')
        users = students.filter(
            student__courseenrollment__course_offered__in=instance.announcement_filters.course.filter(),
            student__program__in=instance.announcement_filters.program.filter(),
            student__semester__in=instance.announcement_filters.semester.filter()
        )
    
    users = users.distinct()
    assign_perm('view_announcement', users, instance)

    if instance.is_global: return

    notify.send(instance.created_by, verb='announce', recipient=users, action_object=instance, description=description, href=href)

post_save.connect(announcement_save_handler, sender=Announcement)
