from django.http.response import HttpResponse, HttpResponseForbidden
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.utils import get_current_student, get_current_teacher, is_teacher
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, FormMixin, CreateView
from meta.views import Meta
from saiki.utils import get_site_title
from .forms import PostCreateForm
import uuid
import course.models
import assignment.models
from django.shortcuts import render, redirect, reverse
from guardian.shortcuts import assign_perm

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'stream/post_delete.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super(PostDeleteView,self).get_context_data(**kwargs)
        course_slug = self.kwargs['slug']

        meta = Meta(
            title=get_site_title(f'Delete Post')
        )
        
        context['is_course_page'] = 'active'
        context['is_stream_page'] = 'active'
        context['meta'] = meta

        try:
            course_offering = course.models.CourseOffering.objects.filter(slug=course_slug)[:1].get()
        except course.models.CourseOffering.DoesNotExist:
            course_offering = None

        context['course'] = course_offering

        return context

    def get(self, request, *args, **kwargs):
        is_teacher = request.user.is_teacher
        is_student = request.user.is_student
        
        if not (is_student or is_teacher):
            return HttpResponseForbidden()
        
        obj = self.get_object()
        
        if is_student:
            student = get_current_student(self.request)

            if not student.user.has_perm('delete_post', obj):
                return HttpResponseForbidden()
        elif is_teacher:
            teacher = get_current_teacher(self.request)

            if not teacher.user.has_perm('delete_post', obj):
                return HttpResponseForbidden()

        return super().get(self, request, *args, **kwargs)  

    def post(self, request, *args, **kwargs):
        is_teacher = request.user.is_teacher
        is_student = request.user.is_student
        
        if not (is_student or is_teacher):
            return HttpResponseForbidden()
        
        obj = self.get_object()
        
        if is_student:
            student = get_current_student(self.request)

            if not student.user.has_perm('delete_post', obj):
                return HttpResponseForbidden()
        elif is_teacher:
            teacher = get_current_teacher(self.request)

            if not teacher.user.has_perm('delete_post', obj):
                return HttpResponseForbidden()

        return super().post(self, request, *args, **kwargs)  

    def get_success_url(self):
        stream_slug = self.kwargs['slug']
        return reverse('course:stream:index', kwargs={'slug': stream_slug})

class PostCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = 'accounts:login'
    template_name = 'stream/post_list.html'
    model = Post
    form_class = PostCreateForm

    def post(self, request, *args, **kwargs):
        is_teacher = request.user.is_teacher
        is_student = request.user.is_student

        stream_slug = self.kwargs['slug']

        try:
            course_offering = course.models.CourseOffering.objects.filter(slug=stream_slug)[:1].get()
        except course.models.CourseOffering.DoesNotExist:
            course_offering = None

        if not (is_student or is_teacher):
            return HttpResponseForbidden()

        if is_student:
            student = get_current_student(self.request)

            if not student.user.has_perm('view_courseoffering', course_offering):
                return HttpResponseForbidden()
        elif is_teacher:
            teacher = get_current_teacher(self.request)

            if not teacher.user.has_perm('view_courseoffering', course_offering):
                return HttpResponseForbidden()

        form = self.form_class(request.POST)

        if form.is_valid():
            obj = Post()
            obj.body = form.cleaned_data['body']
            obj.stream = course_offering
            obj.allow_comments = True
            obj.user = request.user
            obj.save()
        
            return redirect(obj)
        else:
            print('invalid')
            return redirect('course:stream:index', slug=stream_slug)

class PostListView(LoginRequiredMixin, ListView):
    redirect_field_name = 'accounts:login'
    template_name = 'stream/post_list.html'
    model = Post
    context_object_name = 'objects'

    def get(self, request, *args, **kwargs):
        is_teacher = request.user.is_teacher
        is_student = request.user.is_student

        stream_slug = self.kwargs['slug']

        try:
            course_offering = course.models.CourseOffering.objects.filter(slug=stream_slug)[:1].get()
        except course.models.CourseOffering.DoesNotExist:
            course_offering = None

        if is_student:
            student = get_current_student(self.request)

            if not student.user.has_perm('view_courseoffering', course_offering):
                return HttpResponseForbidden()

            return super().get(self, request, *args, **kwargs)
        elif is_teacher:
            teacher = get_current_teacher(self.request)

            if not teacher.user.has_perm('view_courseoffering', course_offering):
                return HttpResponseForbidden()

            return super().get(self, request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def get_context_data(self, **kwargs):
        context = super(PostListView,self).get_context_data(**kwargs)
        context['is_course_page'] = 'active'
        context['is_stream_page'] = 'active'
        course_slug = self.kwargs['slug']


        try:
            course_offering = course.models.CourseOffering.objects.filter(slug=course_slug)[:1].get()
        except course.models.CourseOffering.DoesNotExist:
            course_offering = None

        meta = Meta(
            title=get_site_title(f'Stream - {course_offering.course.code}')
        )
        context['meta'] = meta
        context['course'] = course_offering

        return context

    def get_queryset(self):
        stream_slug = self.kwargs['slug']
        if self.request.user.is_authenticated:
            return Post.objects.filter(stream__slug=stream_slug)
        else:
            return Post.objects.none()

class PostDetailView(LoginRequiredMixin, DetailView):
    redirect_field_name = 'accounts:login'
    template_name = 'stream/post_detail.html'
    model = Post
    context_object_name = 'object'
    slug_url_kwarg = 'post_slug'

    def get(self, request, *args, **kwargs):
        is_teacher = request.user.is_teacher
        is_student = request.user.is_student

        obj = self.get_object()

        if is_student:
            student = get_current_student(self.request)

            if not student.user.has_perm('view_post', obj):
                return HttpResponseForbidden()

            return super().get(self, request, *args, **kwargs)
        elif is_teacher:
            teacher = get_current_teacher(self.request)

            if not teacher.user.has_perm('view_post', obj):
                return HttpResponseForbidden()

            return super().get(self, request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def get_context_data(self, **kwargs):
        context = super(PostDetailView,self).get_context_data(**kwargs)
        context['is_course_page'] = 'active'
        context['is_stream_page'] = 'active'
        course_slug = self.kwargs['slug']

        try:
            course_offering = course.models.CourseOffering.objects.filter(slug=course_slug)[:1].get()
        except course.models.CourseOffering.DoesNotExist:
            course_offering = None

        meta = Meta(
            title=get_site_title(f'Stream - {course_offering.course.code}')
        )
        context['meta'] = meta
        context['course'] = course_offering

        return context

    def get_queryset(self):
        post_slug = self.kwargs['post_slug']
        print(post_slug)
        if self.request.user.is_authenticated:
            return Post.objects.filter(slug=post_slug)
        else:
            return Post.objects.none()