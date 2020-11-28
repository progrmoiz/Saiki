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
from meta.views import Meta
from saiki.utils import get_site_title
from guardian.shortcuts import get_objects_for_user

# add mark as read
class AnnouncementListView(ListView):
    template_name = 'announcement/announcement_list.html'
    model = Announcement
    context_object_name = 'announcement'
    
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AnnouncementListView,self).get_context_data(**kwargs)
        meta = Meta(
            title=get_site_title('Announcements')
        )
        context['is_announcement_page'] = 'active'

        context['meta'] = meta
        return context

    def get_queryset(self):
        today = datetime.datetime.today()

        # current_sem = student.semester
        # enrolled_courses = CourseOffering.objects.filter(courseenrollment__student=student)
        # program = student.program

        # all active announcements
        a = Announcement.objects.filter(start_date__lte=today, end_date__gte=today, active=True)
        a_global = a.filter(is_global=True)
        a_v = get_objects_for_user(self.request.user, 'announcement.view_announcement', with_superuser=False)

        # course 
        # program
        # semester
        # course + program
        # course + semester
        # program + semester
        # course + program + semester


        # course_only = a.filter(
        #     announcement_filters__course__in=enrolled_courses,
        #     announcement_filters__semester=None,
        #     announcement_filters__program=None
        # )
        # semester_only = a.filter(
        #     announcement_filters__course=None,
        #     announcement_filters__semester=current_sem,
        #     announcement_filters__program=None
        # )
        # program_only = a.filter(
        #     announcement_filters__course=None,
        #     announcement_filters__semester=None,
        #     announcement_filters__program=program
        # )
        # course_semester = a.filter(
        #     announcement_filters__course__in=enrolled_courses,
        #     announcement_filters__semester=current_sem,
        #     announcement_filters__program=None
        # )
        # course_program = a.filter(
        #     announcement_filters__course__in=enrolled_courses,
        #     announcement_filters__semester=None,
        #     announcement_filters__program=program
        # )
        # program_semester = a.filter(
        #     announcement_filters__course=None,
        #     announcement_filters__semester=current_sem,
        #     announcement_filters__program=program
        # )
        # course_program_semester = a.filter(
        #     announcement_filters__course__in=enrolled_courses,
        #     announcement_filters__semester=current_sem,
        #     announcement_filters__program=program
        # )

        # semester_only = a.filter(announcement_filters__semester=current_sem)
        # program_related_only = a.filter(announcement_filters__program=program, announcement_filters__semester=None)

        # program_related =  a.filter(announcement_filters__program=program)

        # program_related_with_sem = a.filter(announcement_filters__program=program, announcement_filters__semesters__in=[current_sem])
        
        # student_courses = CourseEnrollment.objects.filter(student=student)
        # student_courses = CourseOffering.objects.filter(courseenrollment__in=student_courses)
        
        # courses_related = a.filter(announcement_filters__course__in=enrolled_courses)

        return (a_global | a_v).distinct()

class AnnouncementDetailView(DetailView):
    template_name = 'announcement/announcement_detail.html'
    model = Announcement
    context_object_name = 'announcement'
    slug_url_kwarg = 'slug'

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if not request.user.has_perm('view_announcement', obj) and not obj.is_global:
            return HttpResponseForbidden()

        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AnnouncementDetailView,self).get_context_data(**kwargs)
        meta = Meta(
            title=get_site_title(f'{self.get_object().title}')
        )
        context['is_announcement_page'] = 'active'

        context['meta'] = meta
        return context

    def get_queryset(self):
        return Announcement.objects.filter(active=True)