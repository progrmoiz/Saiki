from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Announcement, AnnouncementFilter
from university.models import Department
from course.models import CourseEnrollment, CourseOffering
from accounts.utils import get_current_student
from django.db.models import Q, Count, Case, BooleanField
from itertools import chain
import datetime

# Create your views here.
class AnnouncementListView(ListView):
    template_name = 'announcement/announcement.html'
    model = Announcement
    context_object_name = 'announcement'
    ordering = ['tags', '-updated_at']

    def get_context_data(self, **kwargs):
        context = super(AnnouncementListView,self).get_context_data(**kwargs)
        context['is_announcement_page'] = 'active'
        context['student'] = get_current_student(self.request)
        return context

    def get_queryset(self):
        student = get_current_student(self.request)
        today = datetime.datetime.today()

        student_courses = CourseEnrollment.objects.filter(student=student)
        student_courses = CourseOffering.objects.filter(courseenrollment__in=student_courses)

        a = Announcement.objects.filter(start_date__lte=today, end_date__gte=today, active=True)

        a_g = a.filter(is_global=True)
        a_d = a.filter(announcement_filters__department=student.department)
        a_s = a_d.filter(Q(announcement_filters__semesters=[student.semester]))
        a_c = a_d.filter(Q(announcement_filters__course__in=student_courses))

        return (a_g | a_s | a_c | a_d)

class AnnouncementDetailView(DetailView):
    # template_name = 'announcement/announcement_detail.html'
    model = Announcement
    context_object_name = 'announcement'

    def get_context_data(self, **kwargs):
        context = super(AnnouncementDetailView,self).get_context_data(**kwargs)
        context['is_announcement_page'] = 'active'
        context['student'] = get_current_student(self.request)
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Announcement.objects.filter(active=True)
        else:
            return Announcement.objects.none()