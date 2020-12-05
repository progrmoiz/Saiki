from django.shortcuts import render
from .models import ResourceFolder
from accounts.utils import get_current_student, get_current_teacher, is_teacher
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse, HttpResponseForbidden
from meta.views import Meta
from saiki.utils import get_site_title
import course.models
from django.views.generic.detail import DetailView

class ResourceDetailView(LoginRequiredMixin, DetailView):
    redirect_field_name = 'accounts:login'
    template_name = 'resources/resource_detail.html'
    model = ResourceFolder
    context_object_name = 'object'
    slug_url_kwarg = 'slug'
    slug_field = 'course_offering__slug'

    # def get(self, request, *args, **kwargs):
    #     is_teacher = request.user.is_teacher
    #     is_student = request.user.is_student

    #     obj = self.get_object()

    #     if is_student:
    #         student = get_current_student(self.request)

    #         if not student.user.has_perm('view_post', obj):
    #             return HttpResponseForbidden()

    #         return super().get(self, request, *args, **kwargs)
    #     elif is_teacher:
    #         teacher = get_current_teacher(self.request)

    #         if not teacher.user.has_perm('view_post', obj):
    #             return HttpResponseForbidden()

    #         return super().get(self, request, *args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()

    def get_context_data(self, **kwargs):
        context = super(ResourceDetailView,self).get_context_data(**kwargs)
        context['is_course_page'] = 'active'
        context['is_resource_page'] = 'active'
        course_slug = self.kwargs['slug']

        try:
            course_offering = course.models.CourseOffering.objects.filter(slug=course_slug)[:1].get()
        except course.models.CourseOffering.DoesNotExist:
            course_offering = None

        meta = Meta(
            title=get_site_title(f'Resources - {course_offering.course.code}')
        )
        context['meta'] = meta
        context['course'] = course_offering

        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ResourceFolder.objects.filter(parent=None)
        else:
            return ResourceFolder.objects.none()