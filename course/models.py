from django.db import models
from django.db.models.signals import post_delete, post_save
from django.urls.base import reverse
from django.utils.translation import ugettext as _
from shortuuidfield import ShortUUIDField
from notifications.signals import notify
from guardian.shortcuts import assign_perm
from django.urls import reverse
from meta.models import ModelMeta
from saiki.utils import get_site_title

import accounts.models
import university.models
import result.models 

# Create your models here.
class Course(models.Model):
    code = models.CharField(_('code'), max_length=128, primary_key=True)
    description = models.CharField(_('description'), max_length=128)
    units = models.FloatField(_('units'))
    prereq_course = models.ForeignKey('Course', on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey('university.Department', on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.description, self.code)

class CourseOffering(ModelMeta, models.Model):
    term = models.ForeignKey('university.Term', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey('accounts.Teacher', on_delete=models.CASCADE)
    slug = ShortUUIDField(unique=True, editable=False)
    archive = models.BooleanField(_("Archive"), default=False)

    _metadata = {
        'title': 'get_meta_course_code',
        'description': 'get_meta_course_desc',
    }

    def get_meta_course_code(self):
        return get_site_title(self.course.code)

    def get_meta_course_desc(self):
        return self.course.description

    class Meta:
        ordering = ['-term__year', '-term__half', 'course__code']

    def __str__(self):
        return '{} - {}'.format(self.course.code, self.term)


def courseoffering_save_handler(sender, instance, created, **kwargs):
    # add permission to teacher, so only teacher can edit and view this assignment
    if created:
        assign_perm('view_courseoffering', instance.teacher.user, instance)

post_save.connect(courseoffering_save_handler, sender=CourseOffering)

class CourseEnrollment(models.Model):
    course_offered = models.ForeignKey(CourseOffering, on_delete=models.CASCADE)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
    is_hidden = models.BooleanField(default=False)

    def __str__(self):
        return '{} enrolled in {}'.format(self.student, self.course_offered)

def course_enrollment_save_handler(sender, instance, created, **kwargs):
    # users = accounts.models.User.objects.filter(student__courseenrollment__course_offered=instance.course_offering)
    user = accounts.models.User.objects.filter(pk=1)[0] # action taken by (admin can only perform these actions)
    href = reverse('course:detail', kwargs={'slug': instance.course_offered.slug})

    # give permission to student to view course

    if created:
        assign_perm('view_courseoffering', instance.student.user, instance.course_offered)
        
        result.models.Grade(course_enrollment=instance).save()

        description = f'enrolled you in { instance.course_offered.course.code }'
        notify.send(user, verb='enrolled', recipient=instance.student.user, action_object=instance, target=instance.course_offered, description=description, href=href)


def course_enrollment_delete_handler(sender, instance, *args, **kwargs):
    user = accounts.models.User.objects.filter(pk=1)[0] # action taken by (admin can only perform these actions)
    
    description = f'unenrolled you from { instance.course_offered.course.code }'
    notify.send(user, verb='unenrolled', recipient=instance.student.user, action_object=instance, target=instance.course_offered, description=description)

post_save.connect(course_enrollment_save_handler, sender=CourseEnrollment)
post_delete.connect(course_enrollment_delete_handler, sender=CourseEnrollment)
