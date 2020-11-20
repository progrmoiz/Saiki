from result.utils import SemesterGradeHelper
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _

import university.models
import accounts.models
import course.models

class Grade(models.Model):

    GRADE_POINT_EQUIVALENT = (
        (4.00, 'A'),
        (3.67, 'A-'),
        (3.33, 'B+'),
        (3.00, 'B'),
        (2.67, 'B-'),
        (2.33, 'C+'),
        (2.00, 'C'),
        (1.67, 'D'),
        (0.00, 'F'),
    )

    letter_grade = models.FloatField(_('grade'), choices=GRADE_POINT_EQUIVALENT, blank=True, null=True)
    course_enrollment = models.ForeignKey('course.CourseEnrollment', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} - {}'.format(self.course_enrollment.student.user, self.course_enrollment.course_offered.course.code)

def grade_handler(sender, instance, created, **kwargs):
    s, created = SemesterGrade.objects.get_or_create(student=instance.course_enrollment.student, term=instance.course_enrollment.course_offered.term)
    s.semester_gpa = SemesterGradeHelper.get_sgpa(s)
    s.save(force_update=True)

post_save.connect(grade_handler, sender=Grade)

class SemesterGrade(models.Model):

    semester_gpa = models.FloatField(_("semester gpa"), blank=True, null=True)
    term = models.ForeignKey('university.Term', on_delete=models.CASCADE)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.term)   