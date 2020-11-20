from django.contrib import admin
from .models import Grade, SemesterGrade
from django.utils.html import format_html
from django.urls import reverse
from .utils import SemesterGradeHelper
from guardian.admin import GuardedModelAdmin

# Register your models here.

class GradeAdmin(GuardedModelAdmin):
    list_display = ["get_course", "get_student", "get_course_description", "get_term", "letter_grade", "get_units"]
    list_filter = ["course_enrollment__course_offered__term"]
    search_fields = [
        "course_enrollment__course_offered__course__code",
        "course_enrollment__course_offered__course__description",
        "course_enrollment__student__display_name",
        "course_enrollment__student__user__username"
    ]
    ordering = ["course_enrollment__course_offered__term", "course_enrollment__course_offered__course__code"]

    def get_course(self, obj):
        return obj.course_enrollment.course_offered.course.code
    get_course.short_description = "code"

    def get_course_description(self, obj):
        return obj.course_enrollment.course_offered.course.description
    get_course_description.short_description = "course description"

    def get_term(self, obj):
        return obj.course_enrollment.course_offered.term
    get_term.short_description = "Term"

    def get_units(self, obj):
        return obj.course_enrollment.course_offered.course.units
    get_units.short_description = "unit"

    def get_student(self, obj):
        return obj.course_enrollment.student
    get_student.short_description = "student"

class SemesterGradeAdmin(GuardedModelAdmin):
    pass
    # exclude = ["semester_gpa "]
    # readonly_fields = ["semester_gpa" ]
    # list_display = ["term", "get_student", "semester_gpa"]
    # list_filter = ["term"]
    # search_fields = ["student__display_name", "student__user__username"]

    # def get_student(self, obj):
    #     return GradeAdmin.get_student(self, obj)
    # get_student.short_description = "student"

    # def get_grades(self, obj):
    #     return SemesterGradeHelper.get_grades(obj)

    # def cal_gp_earned(self, obj):
    #     return SemesterGradeHelper.cal_gp_earned(obj)

    # # grade weight average as per selected term
    # def get_gwa(self, obj):
    #     return SemesterGradeHelper.get_gwa(obj)

    # def get_total_credit_hour(self, obj):
    #     return SemesterGradeHelper.get_total_credit_hour(obj)

    # # reference https://www.wikihow.com/Calculate-GPA
    # def get_sgpa(self, obj):
    #     return SemesterGradeHelper.get_sgpa(obj)

    # def save_model(self, request, obj, form, change):
    #     obj.semester_gpa = self.get_sgpa(obj)
    #     super().save_model(request, obj, form, change)


admin.site.register(Grade, GradeAdmin)
admin.site.register(SemesterGrade, SemesterGradeAdmin)