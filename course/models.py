from django.db import models
from django.db.models.signals import post_delete, post_save
from django.urls.base import reverse
from django.utils.translation import ugettext as _
from shortuuidfield import ShortUUIDField
from notifications.signals import notify

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

class CourseOffering(models.Model):
    term = models.ForeignKey('university.Term', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey('accounts.Teacher', on_delete=models.CASCADE)
    slug = ShortUUIDField(unique=True, editable=False)
    archive = models.BooleanField(_("Archive"), default=False)

    class Meta:
        ordering = ['-term__year', '-term__half', 'course__code']

    def __str__(self):
        return '{} - {}'.format(self.course.code, self.term)

class CourseEnrollment(models.Model):
    course_offered = models.ForeignKey(CourseOffering, on_delete=models.CASCADE)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)

    def __str__(self):
        return '{} enrolled in {}'.format(self.student, self.course_offered)

    def save(self, *args, **kwargs):
        grade = result.models.Grade(course_offering=self.course_offered, student=self.student)
        grade.save()
        super(CourseEnrollment, self).save(*args, **kwargs) # Call the real save() method


def course_enrollment_save_handler(sender, instance, created, **kwargs):
    # users = accounts.models.User.objects.filter(student__courseenrollment__course_offered=instance.course_offering)
    user = accounts.models.User.objects.filter(pk=1)[0] # action taken by (admin can only perform these actions)
    href = reverse('course_detail', kwargs={'slug': instance.course_offered.slug})

    if created:
        description = f'enrolled you in { instance.course_offered.course.code }'
        notify.send(user, verb='enrolled', recipient=instance.student.user, action_object=instance, target=instance.course_offered, description=description, href=href)

def course_enrollment_delete_handler(sender, instance, *args, **kwargs):
    user = accounts.models.User.objects.filter(pk=1)[0] # action taken by (admin can only perform these actions)
    
    description = f'unenrolled you from { instance.course_offered.course.code }'
    notify.send(user, verb='unenrolled', recipient=instance.student.user, action_object=instance, target=instance.course_offered, description=description)

post_save.connect(course_enrollment_save_handler, sender=CourseEnrollment)
post_delete.connect(course_enrollment_delete_handler, sender=CourseEnrollment)
