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

class CourseStudentRecordView(LoginRequiredMixin, FormMixin, DetailView):
    redirect_field_name = 'login'
    template_name = 'course/course_student_record.html'
    model = CourseOffering
    context_object_name = 'course'
    form_class = GradeForm

    def get_success_url(self):
        slug = self.kwargs['slug']
        username = self.kwargs['username']
        
        return reverse('course_detail', kwargs={'slug': slug})

    def get(self, request, *args, **kwargs):
        teacher = get_current_teacher(self.request)

        if not teacher:
            return HttpResponseForbidden()

        return super().get(self, request, *args, **kwargs)


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
                course_offering=self.object,
                student=student
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
            href = reverse('term', kwargs={'pk': self.object.term.id})

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
        context = super(CourseStudentRecordView,self).get_context_data(**kwargs)
        username = self.kwargs['username']

        context['is_course_page'] = 'active'
        context['grade'] = Grade.objects.filter(course_offering=self.object, student__user__username=username)[0]
        context['student_'] = Student.objects.filter(user__username=username)[0]
        context['form'] = self.form_class()
        context['form']['grade'].initial = context['grade'].letter_grade

        return context

    def get_queryset(self):
        slug = self.kwargs['slug']

        if self.request.user.is_authenticated:
            return CourseOffering.objects.filter(slug=slug)
        else:
            return CourseOffering.objects.none()

# TODO: Cannot be authorized by unenrolled student
class CourseDetailView(LoginRequiredMixin, DetailView):
    redirect_field_name = 'login'
    template_name = 'course/course_detail.html'
    model = CourseOffering
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView,self).get_context_data(**kwargs)
        context['is_course_page'] = 'active'

        if is_teacher:
            context['students'] = Student.objects.filter(courseenrollment__course_offered=self.object, grade__course_offering=self.object)

        return context

    def get_queryset(self):
        slug = self.kwargs['slug']
        if self.request.user.is_authenticated:
            return CourseOffering.objects.filter(slug=slug)
        else:
            return CourseOffering.objects.none()

# # Create your views here.
class CourseListView(LoginRequiredMixin, ListView):
    redirect_field_name = 'login'
    model = CourseOffering
    context_object_name = 'courses_offering'
    template_name = 'course/course.html'
    course_offering = CourseOffering.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        student = get_current_student(self.request)
        teacher = get_current_teacher(self.request)

        context['is_course_page'] = 'active'
        if student:
            letter_grades = [4.00,
                             3.67,
                             3.33,
                             3.00,
                             2.67,
                             2.33,
                             2.00,
                             1.67,
                             0.00]
            
            context['archives'] = CourseOffering.objects.filter(
                courseenrollment__student=student, grade__student=student, grade__letter_grade__in=letter_grades)
        elif teacher:
            context['archives'] = CourseOffering.objects.filter(teacher=teacher, archive=True)

        return context

    def get_queryset(self):
        student = get_current_student(self.request)
        teacher = get_current_teacher(self.request)

        queryset = super(CourseListView, self).get_queryset()
        if student:
            queryset = queryset.filter(courseenrollment__student=student, grade__student=student, grade__letter_grade__isnull=True)
        elif teacher:
            queryset = queryset.filter(teacher=teacher, archive=False)

        return queryset

    # def dispatch(self, request, *args, **kwargs):
    #     student = get_current_student(self.request)

    #     if student.is_graduated:
    #         return redirect('my_grades')
    #     else:
    #         return super(ResultListView, self).dispatch(request, *args, **kwargs)
