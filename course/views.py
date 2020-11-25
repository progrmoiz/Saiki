from django.db.models import query
from course.forms import GradeForm
from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course, CourseOffering, CourseEnrollment
# from university.models import Term
from accounts.utils import get_current_student, get_current_teacher, is_teacher
from accounts.models import Student
from result.models import Grade, SemesterGrade
from django.urls import reverse
from django.contrib import messages
from notifications.signals import notify
from django.views.generic.edit import UpdateView
from meta.views import Meta
from saiki.utils import get_site_title
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CourseOfferingSerializer

class CourseOfferingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CourseOffering.objects.all()
    serializer_class = CourseOfferingSerializer
    lookup_field = 'slug'   
    
class CoursePeopleEditView(LoginRequiredMixin, FormMixin, DetailView):
    redirect_field_name = 'accounts:login'
    template_name = 'course/course_people_edit.html'
    model = CourseOffering
    context_object_name = 'course'
    form_class = GradeForm

    def get(self, request, *args, **kwargs):
        if not request.user.is_teacher:
            return HttpResponseForbidden()
        
        teacher = get_current_teacher(self.request)
        obj = self.get_object()

        if not teacher.user.has_perm('view_courseoffering', obj):
            return HttpResponseForbidden()
            
        return super().get(self, request, *args, **kwargs)

    def get_success_url(self):
        slug = self.kwargs['slug']
        username = self.kwargs['username']
        return reverse('course:detail', kwargs={'slug': slug})

    def post(self, request, *args, **kwargs):
        teacher = get_current_teacher(self.request)

        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        if not teacher:
            return HttpResponseForbidden()

        self.object = self.get_object()
        username = self.kwargs['username']

        student = Student.objects.filter(user__username=username)[0]
        form = GradeForm(request.POST)

        if form.is_valid():
            obj = Grade.objects.filter(
                course_enrollment__student=student,
                course_enrollment__course_offered=self.object
            )[0]
            obj.letter_grade = form.cleaned_data['grade']
            obj.save()

            messages.success(request, f"Student record updated: {username}")
            if obj.letter_grade == None:
                verb = "ungraded"
                s = ""
            else:
                verb = "graded "
                s = f" <b>{ obj.letter_grade } GPA</b>"
                
            description = f"{ verb }{ s } in { self.object.course.code }"
            href = reverse('result:by_term', kwargs={'pk': self.object.term.id})

            notify.send(teacher.user, verb=verb, recipient=student.user, action_object=obj, target=self.object, description=description, href=href)

            return self.form_valid(form)
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
                
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super(CoursePeopleEditView,self).get_context_data(**kwargs)
        username = self.kwargs['username']
        student = Student.objects.filter(user__username=username)[0]

        context['is_course_page'] = 'active'
        context['is_people_page'] = 'active'
        context['meta'] = self.get_object().as_meta(self.request)
        context['grade'] = Grade.objects.filter(course_enrollment__course_offered=self.object, course_enrollment__student=student)[0]
        context['student_'] = student
        context['form'] = self.form_class()
        context['form']['grade'].initial = context['grade'].letter_grade

        return context

    def get_queryset(self):
        slug = self.kwargs['slug']

        if self.request.user.is_authenticated:
            return CourseOffering.objects.filter(slug=slug)
        else:
            return CourseOffering.objects.none()

class CoursePeopleView(LoginRequiredMixin, DetailView):
    redirect_field_name = 'accounts:login'
    template_name = 'course/course_people_list.html'
    model = CourseOffering
    context_object_name = 'course'

    def get(self, request, *args, **kwargs):
        is_teacher = request.user.is_teacher
        is_student = request.user.is_student

        obj = self.get_object()

        if is_student:
            student = get_current_student(self.request)

            if not student.user.has_perm('view_courseoffering', obj):
                return HttpResponseForbidden()

            return super().get(self, request, *args, **kwargs)
        elif is_teacher:
            teacher = get_current_teacher(self.request)

            if not teacher.user.has_perm('view_courseoffering', obj):
                return HttpResponseForbidden()

            return super().get(self, request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def get_context_data(self, **kwargs):
        context = super(CoursePeopleView,self).get_context_data(**kwargs)
        context['is_course_page'] = 'active'
        context['is_people_page'] = 'active'
        meta = Meta(
            title=get_site_title(f'People - { self.get_object().course.code }')
        )

        context['is_course_page'] = 'active'
        context['meta'] = meta

        if is_teacher:
            context['students'] = Student.objects.filter(courseenrollment__course_offered=self.object)

        return context

    def get_queryset(self):
        slug = self.kwargs['slug']
        if self.request.user.is_authenticated:
            return CourseOffering.objects.filter(slug=slug)
        else:
            return CourseOffering.objects.none()

# TODO: Cannot be authorized by unenrolled student
class CourseDetailView(LoginRequiredMixin, DetailView):
    redirect_field_name = 'accounts:login'
    template_name = 'course/course_detail.html'
    model = CourseOffering
    context_object_name = 'course'

    def get(self, request, *args, **kwargs):
        is_teacher = request.user.is_teacher
        is_student = request.user.is_student

        obj = self.get_object()

        if is_student:
            student = get_current_student(self.request)

            if not student.user.has_perm('view_courseoffering', obj):
                return HttpResponseForbidden()

            return redirect('course:stream:index', slug=obj.slug)
        elif is_teacher:
            teacher = get_current_teacher(self.request)

            if not teacher.user.has_perm('view_courseoffering', obj):
                return HttpResponseForbidden()
            
            return redirect('course:stream:index', slug=obj.slug)
        else:
            return HttpResponseForbidden()

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView,self).get_context_data(**kwargs)
        context['is_course_page'] = 'active'
        context['meta'] = self.get_object().as_meta(self.request)

        if is_teacher:
            context['students'] = Student.objects.filter(courseenrollment__course_offered=self.object)

        return context

    def get_queryset(self):
        slug = self.kwargs['slug']
        if self.request.user.is_authenticated:
            return CourseOffering.objects.filter(slug=slug)
        else:
            return CourseOffering.objects.none()

# # Create your views here.
class CourseListView(LoginRequiredMixin, ListView):
    redirect_field_name = 'accounts:login'
    model = CourseOffering
    context_object_name = 'courses_offering'
    template_name = 'course/course_list.html'
    course_offering = CourseOffering.objects.all()

    def get(self, request, *args, **kwargs):
        if not (request.user.is_teacher or request.user.is_student):
            return HttpResponseForbidden()

        return super().get(self, request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        student = get_current_student(self.request)
        teacher = get_current_teacher(self.request)
        meta = Meta(
            title=get_site_title('Courses')
        )

        context['is_course_page'] = 'active'
        context['meta'] = meta
        if student:
            context['hidden_courses'] = CourseOffering.objects.filter(
                courseenrollment__student=student, courseenrollment__is_hidden=True)
        elif teacher:
            context['archives'] = CourseOffering.objects.filter(teacher=teacher, archive=True)

        return context

    def get_queryset(self):
        student = get_current_student(self.request)
        teacher = get_current_teacher(self.request)

        queryset = super(CourseListView, self).get_queryset()
        if student:
            queryset = queryset.filter(courseenrollment__student=student, courseenrollment__is_hidden=False)
        elif teacher:
            queryset = queryset.filter(teacher=teacher, archive=False)

        return queryset

    # def dispatch(self, request, *args, **kwargs):
    #     student = get_current_student(self.request)

    #     if student.is_graduated:
    #         return redirect('result:select_term')
    #     else:
    #         return super(ResultListView, self).dispatch(request, *args, **kwargs)

class CourseHideFormView(LoginRequiredMixin, UpdateView):
    model = CourseEnrollment
    fields = ['is_hidden'] 
    template_name = 'course_hide_form.html' 
    
    def get_success_url(self):
        return reverse('course:index')


