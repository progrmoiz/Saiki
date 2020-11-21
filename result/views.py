from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.list import ListView
from .models import Grade, SemesterGrade
from university.models import Term
from accounts.utils import get_current_student
from meta.views import Meta
from saiki.utils import get_site_title

class ResultListView(LoginRequiredMixin, ListView):
    redirect_field_name = 'accounts:login'
    model = Grade
    context_object_name = 'grades'
    template_name = 'result/result.html'
    semester_grade = SemesterGrade.objects.all()
    cgpa = 0

    def get(self, request, *args, **kwargs):
        if not request.user.is_student:
            return HttpResponseForbidden()

        return super().get(self, request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(ResultListView, self).get_context_data(**kwargs)
        meta = Meta(
            title=get_site_title('Results')
        )
        

        context['is_result_page'] = 'active'
        context['meta'] = meta
        context['student'] = get_current_student(self.request)
        context['semester_grades'] = self.semester_grade
        context['cgpa'] = self.cgpa
        return context

    def get_queryset(self):
        student = get_current_student(self.request)

        try:
            term = Term.objects.all()[:1].get()
        except Term.DoesNotExist:
            term = None

        #  hterm is None here so get the latest
        self.cgpa = student.get_cgpa()

        queryset = super(ResultListView, self).get_queryset()
        queryset = queryset.filter(course_enrollment__student=student, course_enrollment__course_offered__term=term)
        self.semester_grade = self.semester_grade.filter(student=student, term=term)

        return queryset

    def dispatch(self, request, *args, **kwargs):
        student = get_current_student(self.request)

        if student.is_graduated:
            return redirect('result:select_term')
        else:
            return super(ResultListView, self).dispatch(request, *args, **kwargs)

class ViewMyGrades(LoginRequiredMixin, ListView):
    redirect_field_name = 'accounts:login'
    model = SemesterGrade
    template_name='result/my_grades.html'
    semester_grades = None
    term = None

    def get(self, request, *args, **kwargs):
        if not request.user.is_student:
            return HttpResponseForbidden()

        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ViewMyGrades, self).get_context_data(**kwargs)
        meta = Meta(
            title=get_site_title('Select Term')
        )

        context['is_result_page'] = 'active'
        context['meta'] = meta
        
        context['student'] = get_current_student(self.request)
        context['semester_grades'] = self.semester_grades
        context['term'] = self.term
        return context

    def get_queryset(self):
        student = get_current_student(self.request)

        if not student.is_graduated:
            try:
                self.term = Term.objects.all()[:1].get()
            except Term.DoesNotExist:
                self.term = None

        self.cgpa = student.get_cgpa()
        self.semester_grades = student.get_semester_grades()
        queryset = super(ViewMyGrades, self).get_queryset()
        queryset = queryset
        return queryset

class SelectedTerm(LoginRequiredMixin, ListView):
    redirect_field_name = 'accounts:login'
    model = Grade
    context_object_name = 'grades'
    template_name = 'result/result.html'
    semester_grade = SemesterGrade.objects.all()
    cgpa = 0

    def get(self, request, *args, **kwargs):
        if not request.user.is_student:
            return HttpResponseForbidden()

        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SelectedTerm, self).get_context_data(**kwargs)
        try:
            term = Term.objects.filter(pk=self.kwargs['pk'])[:1].get()
        except Term.DoesNotExist:
            term = None
        
        title = f'Result - {term}'
        if not term:
            title = 'Result'

        meta = Meta(
            title=get_site_title(title)
        )

        context['is_result_page'] = 'active'
        context['meta'] = meta

        context['student'] = get_current_student(self.request)
        context['semester_grade'] = self.semester_grade[:1].get()
        context['cgpa'] = self.cgpa
        return context

    def get_queryset(self):
        student = get_current_student(self.request)

        try:
            term = Term.objects.filter(pk=self.kwargs['pk'])[:1].get()
        except Term.DoesNotExist:
            term = None

        queryset = super(SelectedTerm, self).get_queryset()
        queryset = queryset.filter(course_enrollment__student=student, course_enrollment__course_offered__term=term)

        self.semester_grade = self.semester_grade.filter(student=student, term=term)
        self.cgpa = student.get_cgpa(self.semester_grade[:1].get())

        return queryset
