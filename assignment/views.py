from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Student
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, FormMixin, CreateView
from django.http import HttpResponseForbidden, HttpResponseNotFound
from datetime import datetime
import uuid
from django.shortcuts import redirect
from django.template.defaultfilters import pluralize
from notifications.signals import notify

from course.models import CourseOffering

from .forms import AssignPointForm, AssignmentEditForm, AssignmentMaterialForm, AssignmentSubmissionForm, AssignmentCreateForm
from .models import Assignment, AssignmentFile, AssignmentWork, AssignmentWorkFile
from accounts.utils import get_current_student, get_current_teacher, is_student
import course.models

class AssignStudentPointView(LoginRequiredMixin, FormMixin, DetailView):
    redirect_field_name = 'login'
    template_name = 'assignment/assign_student_point.html'
    model = Assignment
    context_object_name = 'assignment'
    form_class = AssignPointForm

    def get_success_url(self):
        slug = self.kwargs['slug']
        username = self.kwargs['username']

        return reverse('assignment_detail', kwargs={'slug': slug})

    def get(self, request, *args, **kwargs):
        teacher = get_current_teacher(self.request)

        if not teacher:
            return HttpResponseForbidden()

        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AssignStudentPointView,self).get_context_data(**kwargs)
        student = get_current_student(self.request)
        teacher = get_current_teacher(self.request)
        slug = self.kwargs['slug']
        username = self.kwargs['username']

        context['is_assignment_page'] = 'active'
        context['submission'] = AssignmentWorkFile.objects.filter(assignment_work__assignment__slug=slug, assignment_work__student__user__username=username)
        context['materials'] = AssignmentFile.objects.filter(assignment__slug=slug)
        context['student_'] = Student.objects.filter(user__username=username)[0]
        context['assignment_work'] = AssignmentWork.objects.filter(assignment__slug=slug, student__user__username=username)[0]
        context['form'] = self.form_class()
        context['form']['points'].initial = context['assignment_work'].points

        return context

    def post(self, request, *args, **kwargs):
        teacher = get_current_teacher(self.request)

        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        if not teacher:
            return HttpResponseForbidden()

        self.object = self.get_object()
        username = self.kwargs['username']
        slug = self.kwargs['slug']

        student = Student.objects.filter(user__username=username)[0]
        form = AssignPointForm(request.POST)

        if form.is_valid():
            obj = AssignmentWork.objects.filter(assignment__slug=slug, student__user__username=username)[0]
            obj.points = form.cleaned_data['points']
            obj.save()

            if obj.points != -1:
                messages.success(request, f"Assigned {obj.points} point{pluralize(obj.points)} to {username}")
            else:
                messages.info(request, f"Assignment ungraded for {username}")
            
            description = f"returned <b>{ self.object.title }</b> in { self.object.course_offering.course.code }"
            href = reverse('assignment_detail', kwargs={'slug': self.object.slug})

            notify.send(teacher.user, verb='returned', recipient=student.user, action_object=self.object, target=self.object.course_offering, description=description, href=href)

            return self.form_valid(form)
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
                
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super().form_valid(form)

    def get_queryset(self):
        queryset = super(AssignStudentPointView, self).get_queryset()
        queryset = queryset.filter()

        return queryset

class AssignmentListView(LoginRequiredMixin, ListView):
    redirect_field_name = 'login'
    model = Assignment
    context_object_name = 'assignments'
    template_name = 'assignment/assignment.html'

    def get_context_data(self, **kwargs):
        context = super(AssignmentListView, self).get_context_data(**kwargs)
        student = get_current_student(self.request)
        teacher = get_current_teacher(self.request)
        context['is_assignment_page'] = 'active'
        
        course_slug = self.kwargs.get('slug')
        print("hello", course_slug)

        try:
            course_offering = course.models.CourseOffering.objects.filter(slug=course_slug)[:1].get()
        except course.models.CourseOffering.DoesNotExist:
            course_offering = None

        context['course'] = course_offering

        if student:
            if not course_slug:
                context['assignments_submitted'] = AssignmentWork.objects.filter(assignment__course_offering__grade__letter_grade__isnull=True, student=student, submitted=True).order_by('-submit_date')
            else:
                context['assignments_submitted'] = AssignmentWork.objects.filter(student=student, submitted=True, assignment__course_offering=course_offering)

            
        elif teacher:
            if not course_slug:
                context['courses'] = course.models.CourseOffering.objects.filter(teacher=teacher, archive=False)
        
        return context

    def get_queryset(self):
        student = get_current_student(self.request)
        teacher = get_current_teacher(self.request)
        course_slug = self.kwargs.get('slug')
        
        queryset = super(AssignmentListView, self).get_queryset()

        try:
            course_offering = course.models.CourseOffering.objects.filter(slug=course_slug)[:1].get()
        except course.models.CourseOffering.DoesNotExist:
            course_offering = None
        
        if student:
            if not course_slug:
                queryset = queryset.filter(course_offering__grade__student=student,course_offering__grade__letter_grade__isnull=True, 
                course_offering__courseenrollment__student=student).exclude(assignmentwork__student=student, assignmentwork__submitted=True).order_by('deadline')
            else:
                queryset = queryset.filter(course_offering=course_offering, course_offering__courseenrollment__student=student).exclude(assignmentwork__student=student, assignmentwork__submitted=True)
        elif teacher:
            if not course_slug:
                queryset = queryset.filter(course_offering__teacher=teacher, course_offering__archive=False)
            else:
                queryset = queryset.filter(course_offering__teacher=teacher, course_offering__archive=False, course_offering=course_offering)

        return queryset

class AssignmentDetailView(LoginRequiredMixin, FormMixin, DetailView):
    redirect_field_name = 'login'
    template_name = 'assignment/assignment_detail.html'
    model = Assignment
    context_object_name = 'assignment'
    form_class = AssignmentSubmissionForm

    def get_success_url(self):
        slug = self.kwargs.get('slug')

        return reverse('assignment', kwargs={'slug': slug})

    def get(self, request, *args, **kwargs):
        student = get_current_student(self.request)
        teacher = get_current_teacher(self.request)

        if student:
            object = self.get_object()
            self.asgmt_work, _created = AssignmentWork.objects.get_or_create(assignment=self.get_object(), student=student)
        elif teacher:
            pass

        return super().get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        turn = request.POST.get('turn')

        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        # self.object = self.get_object()
        # form = self.get_form()
        self.student = get_current_student(self.request)
        self.object = self.get_object()
        print("POST OBJECT", self.object)
        
        slug = self.kwargs['slug']
        print(args)
        print(kwargs)
        # context['work_files'] = AssignmentWorkFile.objects.filter(assignment_work__assignment__slug=slug, assignment_work__student=context['student'])
        print("POST slug", slug)

        self.asgmt_work, _created = AssignmentWork.objects.get_or_create(assignment=self.object, student=self.student)

        print("POST self.asgmt_work", self.asgmt_work)

        if turn == "True":
            self.asgmt_work.submitted = True
            self.asgmt_work.submit_date = datetime.now()
            self.asgmt_work.save()
        elif turn == "False":
            self.asgmt_work.submitted = False
            self.asgmt_work.save() 

        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            print("valid")
            instance = form.save(commit=False)
            print("FORM", form)
            print("HELLO2", self.asgmt_work)
            instance.assignment_work = self.asgmt_work
            print("HELLO", instance.assignment_work)
            instance.save()


            return self.form_valid(form)
        else:
            print("invalid")

            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AssignmentDetailView,self).get_context_data(**kwargs)
        student = get_current_student(self.request)
        teacher = get_current_teacher(self.request)

        context['is_assignment_page'] = 'active'
        
        if student:
            # context['student'] = self.student
            context['form'] = AssignmentSubmissionForm
            slug = self.kwargs['slug']
            context['work_files'] = AssignmentWorkFile.objects.filter(assignment_work__assignment__slug=slug, assignment_work__student=student)
            context['materials'] = AssignmentFile.objects.filter(assignment__slug=slug)

            # print(context['work_files'])
            # print(slug)
            object = self.get_object()
            context['work'] = self.asgmt_work
            context['turned'] = self.asgmt_work.submitted
        elif teacher:
            context['students'] = Student.objects.filter(assignmentwork__submitted=True, assignmentwork__assignment=self.object)

        return context

    def form_valid(self, form):
        return super(AssignmentDetailView, self).form_valid(form)

    def get_queryset(self):
        student = get_current_student(self.request)
        
        queryset = super(AssignmentDetailView, self).get_queryset()
        queryset = queryset.filter()

        return queryset

class AssignmentCreateView(LoginRequiredMixin, FormMixin, DetailView):
    redirect_field_name = 'login'
    template_name = 'assignment/assignment_create.html'
    model = course.models.CourseOffering
    context_object_name = 'course'
    form_class = AssignmentCreateForm
    assignment_slug = uuid.uuid4()

    def get_success_url(self):
        # slug = self.kwargs['slug']
        # username = self.kwargs['username']

        # print(slug)
      
        return reverse('assignment_edit', kwargs={'slug': self.assignment_slug})

    def get(self, request, *args, **kwargs):
        teacher = get_current_teacher(self.request)
        # self.assignment_slug = uuid.uuid4()

        if not teacher:
            return HttpResponseForbidden()

        return super().get(self, request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        teacher = get_current_teacher(self.request)

        if not teacher:
            return HttpResponseForbidden()

        form = self.form_class(request.POST)

        if form.is_valid():
            obj = Assignment()
            obj.title = form.cleaned_data['title']
            obj.points = form.cleaned_data['points']
            dt = form.cleaned_data['date']
            tm = form.cleaned_data['time']
            obj.deadline = datetime.combine(dt, tm)
            obj.description = form.cleaned_data['description']
            # obj.slug = self.assignment_slug
            self.assignment_slug = uuid.uuid4()
            obj.slug = self.assignment_slug
            obj.created = datetime.now()
            obj.modified = datetime.now()
            obj.course_offering = self.object
            obj.save()
            
            messages.success(request, f"Assignment created")
            return self.form_valid(form)
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AssignmentCreateView,self).get_context_data(**kwargs)
        teacher = get_current_teacher(self.request)
        context['is_assignment_page'] = 'active'
        return context

    def form_valid(self, form):
        return super(AssignmentCreateView, self).form_valid(form) 

    def get_queryset(self):
        queryset = super(AssignmentCreateView, self).get_queryset()
        queryset = queryset.filter()

        return queryset

class AssignmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Assignment
    template_name = 'assignment/assignment_delete.html'

    def get(self, request, *args, **kwargs):
        teacher = get_current_teacher(self.request)

        if not teacher:
            return HttpResponseForbidden()
        
        return super().get(self, request, *args, **kwargs)  

    def post(self, request, *args, **kwargs):
        teacher = get_current_teacher(self.request)

        if not teacher:
            return HttpResponseForbidden()
        
        return super().post(self, request, *args, **kwargs)  

    def get_success_url(self):
        return reverse('assignment')

class AssignmentEditUploadView(LoginRequiredMixin, FormMixin, DetailView):
    redirect_field_name = 'login'
    model = Assignment
    context_object_name = 'assignment'
    form_class = AssignmentMaterialForm

    def get_success_url(self):
        slug = self.kwargs.get('slug')

        return reverse('assignment_edit', kwargs={'slug': slug})

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')

        return redirect('assignment_edit', slug=slug)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        slug = self.kwargs.get('slug')
        
        teacher = get_current_teacher(self.request)

        if not teacher:
            return HttpResponseForbidden()

        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.assignment = self.object
            instance.save()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super(AssignmentEditUploadView, self).form_valid(form)

class AssignmentEditView(LoginRequiredMixin, FormMixin, DetailView):
    redirect_field_name = 'login'
    template_name = 'assignment/assignment_edit.html'
    model = Assignment
    context_object_name = 'assignment'
    form_class = AssignmentEditForm

    def get_success_url(self):
        slug = self.kwargs.get('slug')

        return reverse('assignment_edit', kwargs={'slug': slug})

    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        slug = self.kwargs.get('slug')
        
        teacher = get_current_teacher(self.request)

        if not teacher:
            return HttpResponseForbidden()

        form = self.form_class(request.POST)

        if form.is_valid():
            obj = Assignment.objects.filter(slug=slug)[0]
            obj.title = form.cleaned_data['title']
            obj.points = form.cleaned_data['points']
            dt = form.cleaned_data['date']
            tm = form.cleaned_data['time']
            obj.deadline = datetime.combine(dt, tm)
            obj.description = form.cleaned_data['description']
            obj.modified = datetime.now()
            obj.save()
           
            messages.success(request, f"Assignment updated")
            return self.form_valid(form)
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
                
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AssignmentEditView,self).get_context_data(**kwargs)
        teacher = get_current_teacher(self.request)

        context['is_assignment_page'] = 'active'
        context['assignment_files'] = AssignmentFile.objects.filter(assignment=self.object)
        context['form'] = self.form_class()

        return context

    def form_valid(self, form):
        return super(AssignmentEditView, self).form_valid(form)

    def get_queryset(self):
        queryset = super(AssignmentEditView, self).get_queryset()
        queryset = queryset.filter()

        return queryset
