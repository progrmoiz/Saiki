from django.db import models
from django.utils.translation import ugettext as _
from university.models import Term
from course.models import CourseOffering
from accounts.models import Student


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
    course_offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.student.user, self.course_offering.course.code)


class SemesterGrade(models.Model):

    semester_gpa = models.FloatField(_("semester gpa"), blank=True, null=True)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.term)