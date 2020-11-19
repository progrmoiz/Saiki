from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from .models import Grade, SemesterGrade
from university.models import Term
from accounts.utils import get_current_student

# Create your views here.
class ResultListView(ListView):
    model = Grade
    context_object_name = 'grades'
    template_name = 'result/result.html'
    semester_grade = SemesterGrade.objects.all()
    cgpa = 0

    def get_context_data(self, **kwargs):
        context = super(ResultListView, self).get_context_data(**kwargs)
        context['is_result_page'] = 'active'
        context['student'] = get_current_student(self.request)
        context['semester_grade'] = self.semester_grade
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
        queryset = queryset.filter(student=student, course_offering__term=term)
        self.semester_grade = self.semester_grade.filter(student=student, term=term)

        return queryset

    def dispatch(self, request, *args, **kwargs):
        student = get_current_student(self.request)

        if student.is_graduated:
            return redirect('my_grades')
        else:
            return super(ResultListView, self).dispatch(request, *args, **kwargs)

class ViewMyGrades(ListView):
    model = SemesterGrade
    template_name='result/my_grades.html'
    semester_grades = None
    term = None

    def get_context_data(self, **kwargs):
        context = super(ViewMyGrades, self).get_context_data(**kwargs)
        context['is_result_page'] = 'active'
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

class SelectedTerm(ListView):
    model = Grade
    context_object_name = 'grades'
    template_name = 'result/selected_term.html'
    semester_grade = SemesterGrade.objects.all()
    cgpa = 0

    def get_context_data(self, **kwargs):
        context = super(SelectedTerm, self).get_context_data(**kwargs)
        context['is_result_page'] = 'active'
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
        queryset = queryset.filter(student=student, course_offering__term=term)

        self.semester_grade = self.semester_grade.filter(student=student, term=term)
        self.cgpa = student.get_cgpa(self.semester_grade[:1].get())

        return queryset
