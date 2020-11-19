from django.contrib import admin
from .models import Course, CourseOffering, CourseEnrollment
from django.utils.html import format_html

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ["code", "description", "units", "prereq_course_code", "department"]
    search_fields = [
        'course__description',
        'course__code'
    ]
    list_filter = ['course__department']

    def prereq_course_code(self, obj):
        if obj.prereq_course:
            return format_html("<a href='{url}'>{url}</a>", url=obj.prereq_course.code)
        else:
            return None
    prereq_course_code.short_description = "Prereq Course Code"

class CourseOfferingAdmin(admin.ModelAdmin):
    list_display = ["term", "course", "slug"]

class CourseEnrollmentAdmin(admin.ModelAdmin):
    search_fields = [
        'student__display_name', 
        'student__user__first_name', 
        'student__user__last_name',
        'student__user__username',
        'course_offered__course__description',
        'course_offered__course__code'
    ]
    list_filter = ['course_offered__course__department', 'course_offered__term']
    list_display = ["course_offered", "get_student_id", "get_author"]
    
    def get_author(self, obj):
        return obj.course_offered.course.department
    get_author.short_description = 'Department'
    get_author.admin_order_field = 'course_offered__course__department'

    def get_student_id(self, obj):
        return obj.student.user.username
    get_student_id.short_description = 'Student ID'

admin.site.register(Course, CourseAdmin)
admin.site.register(CourseOffering, CourseOfferingAdmin)
admin.site.register(CourseEnrollment, CourseEnrollmentAdmin)