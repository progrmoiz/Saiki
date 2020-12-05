from django.db import models
from django.urls import reverse
import uuid
import os
from shortuuidfield import ShortUUIDField
from django.db.models.signals import post_delete, post_save
from guardian.shortcuts import assign_perm
import accounts.models

class ResourceFolder(models.Model):
    course_offering = models.ForeignKey('course.CourseOffering', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=256)
    parent = models.ForeignKey('resources.ResourceFolder', on_delete=models.CASCADE, blank=True, null=True)
    slug = ShortUUIDField(unique=True, editable=False)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    # def __str__(self):
    #     return ''

    # def get_absolute_url(self):
    #     return ''

def resourcefolder_save_handler(sender, instance, created, **kwargs):
    users = accounts.models.User.objects.filter(student__courseenrollment__course_offered=instance.course_offering)
    
    if created:
        assign_perm('change_resourcefolder', instance.user, instance)
        assign_perm('delete_resourcefolder', instance.user, instance)
        assign_perm('view_resourcefolder', users, instance)
        
        if instance.user.is_teacher:
            assign_perm('view_resourcefolder', instance.user, instance)

        if instance.user.is_student:
            teacher = instance.course_offering.teacher.user
            assign_perm('view_resourcefolder', teacher, instance)
            assign_perm('change_resourcefolder', teacher, instance)
            assign_perm('delete_resourcefolder', teacher, instance)

post_save.connect(resourcefolder_save_handler, sender=ResourceFolder)

def upload_path(instance, filename):
    instance.name = filename

    return os.path.join('resources', instance.folder.course_offering.slug, f'{instance.slug}-{filename}')

class ResourceFile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = ShortUUIDField(unique=True, editable=False)
    file = models.FileField(upload_to=upload_path, blank=True, null=True)
    folder = models.ForeignKey('resources.ResourceFolder', on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)


def resourcefile_save_handler(sender, instance, created, **kwargs):
    users = accounts.models.User.objects.filter(student__courseenrollment__course_offered=instance.folder.course_offering)
    
    if created:
        assign_perm('change_resourcefile', instance.user, instance)
        assign_perm('delete_resourcefile', instance.user, instance)
        assign_perm('view_resourcefile', instance.user, instance)

        if instance.user.is_teacher:
            assign_perm('view_resourcefile', instance.user, instance)

        if instance.user.is_student:
            teacher = instance.folder.course_offering.teacher.user
            assign_perm('view_resourcefile', teacher, instance)
            assign_perm('change_resourcefile', teacher, instance)
            assign_perm('delete_resourcefile', teacher, instance)

post_save.connect(resourcefile_save_handler, sender=ResourceFile)
