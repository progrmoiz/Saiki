from django.db import models
from accounts.models import User
from university.models import Department
from course.models import CourseOffering
from django.utils.translation import ugettext as _
from django import forms
from multiselectfield import MultiSelectField

# https://stackoverflow.com/questions/4670783/make-the-user-in-a-model-default-to-the-current-user

# Create your models here.

class AnnouncementFilter(models.Model):
    title = models.CharField(_('title'), max_length=128, default='Untitled Filter')
    department = models.ManyToManyField(Department, blank=True)
    course = models.ManyToManyField(CourseOffering, blank=True)
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
    semesters = MultiSelectField(_('semesters'), choices=SEMESTER_CHOICES, blank=True, null=True)

    def get_departments(self):
        return ", ".join([p.code for p in self.department.all()])
    get_departments.short_description = 'Departments'

    def get_courses(self):
        return ", ".join([str(p) for p in self.course.all()])
    get_courses.short_description = 'Courses Enrolled'

    def __str__(self):
        return '[{}] {}'.format(self.id, self.title)

class Announcement(models.Model):
    title = models.CharField(_('title'), max_length=128)
    description = models.TextField(_('description'), blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    start_date = models.DateTimeField(_('start date'))
    end_date = models.DateTimeField(_('end date'))

    # is global implies urgent
    is_global = models.BooleanField(_('is global'), default=False, help_text="If global is checked announcement filter will not work.")
    is_draft = models.BooleanField(_('is draft'), default=True)

    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    announcement_filters = models.ManyToManyField(AnnouncementFilter)

    class Meta:
        ordering = ['-updated_at', '-created_at', '-start_date', '-end_date']