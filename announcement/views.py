from django.http.response import HttpResponseForbidden
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Announcement, AnnouncementFilter
from university.models import Program
from course.models import CourseEnrollment, CourseOffering
from accounts.utils import get_current_student
from django.db.models import Q, Count, Case, BooleanField
from itertools import chain
import datetime
from django.http import HttpResponse
from notifications.signals import notify

# add mark as read
class AnnouncementListView(LoginRequiredMixin, ListView):
    redirect_field_name = 'login'
    template_name = 'announcement/announcement.html'
    model = Announcement
    context_object_name = 'announcement'
    
    def get(self, request, *args, **kwargs):
        student = get_current_student(self.request)

        # notify.send(student.user, recipient=student.user, verb='you reached level 10')

        if not student:
            return HttpResponseForbidden()

        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AnnouncementListView,self).get_context_data(**kwargs)
        context['is_announcement_page'] = 'active'
        # context['student'] = get_current_student(self.request)
        return context

    def get_queryset(self):
        student = get_current_student(self.request)
        today = datetime.datetime.today()

        student_courses = CourseEnrollment.objects.filter(student=student)
        student_courses = CourseOffering.objects.filter(courseenrollment__in=student_courses)

        a = Announcement.objects.filter(start_date__lte=today, end_date__gte=today, active=True)

        a_g = a.filter(is_global=True)
        a_d = a.filter(announcement_filters__program=student.program)
        a_s = a_d.filter(Q(announcement_filters__semesters=[student.semester]))
        a_c = a_d.filter(Q(announcement_filters__course__in=student_courses))

        return (a_g | a_s | a_c | a_d).order_by('-start_date')

class AnnouncementDetailView(DetailView):
    template_name = 'announcement/announcement_detail.html'
    model = Announcement
    context_object_name = 'announcement'

    def get(self, request, *args, **kwargs):
        student = get_current_student(self.request)

        if not student:
            return HttpResponse(status=403)

        return super().get(self, request, *args, **kwargs)

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