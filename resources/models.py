from django.db import models
from django.urls import reverse
import uuid
import os
from shortuuidfield import ShortUUIDField

class ResourceFolder(models.Model):
    course_offering = models.ForeignKey('course.CourseOffering', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=256)
    parent = models.ForeignKey('resources.ResourceFolder', on_delete=models.CASCADE, blank=True, null=True)
    slug = ShortUUIDField(unique=True, editable=False)
    
    # def __str__(self):
    #     return ''

    # def get_absolute_url(self):
    #     return ''

# TODO: change this upload path
def upload_path(instance, filename):
    return os.path.join('resources', filename)

class ResourceFile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=upload_path, blank=True, null=True)
    folder = models.ForeignKey('resources.ResourceFolder', on_delete=models.CASCADE)
    slug = ShortUUIDField(unique=True, editable=False)
