from django.db import models
from accounts.models import Student, Teacher
from university.models import Department, Term
from django.utils.translation import ugettext as _

# Create your models here.
class Course(models.Model):
    code = models.CharField(_('code'), max_length=128, primary_key=True)
    description = models.CharField(_('description'), max_length=128)
    units = models.FloatField(_('units'))
    prereq_course = models.ForeignKey('Course', on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({})'.format(self.description, self.code)

class CourseOffering(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-term__year', '-term__half', 'course__code']

    def __str__(self):
        return '{} - {}'.format(self.course.code, self.term)

class CourseEnrollment(models.Model):
    course_offered = models.ForeignKey(CourseOffering, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return '{} enrolled in {}'.format(self.student, self.course_offered)