from django.contrib import admin
from .models import Assignment, AssignmentFile, AssignmentWork, AssignmentFile, AssignmentWorkFile
from guardian.admin import GuardedModelAdmin

# Register your models here.

class AssignmentAdmin(GuardedModelAdmin):
    list_display = ['title', 'get_term',  'get_course', 'get_teacher', 'deadline']
    list_filter = ['course_offering__term', 'course_offering__course__code']
    search_fields = [
        "course_offering__course__code",
        "course_offering__course__description",
    ]

    ordering = ["course_offering__term", "course_offering__course__code"]

    def get_term(self, obj):
        return obj.course_offering.term
    get_term.short_description = "Term"

    def get_course(self, obj):
        return obj.course_offering.course.code
    get_course.short_description = "code"

    def get_teacher(self, obj):
        return obj.course_offering.teacher
    get_teacher.short_description = "Teacher"

class AssignmentWorkAdmin(GuardedModelAdmin):
    list_display = ['assignment', 'student',  'submit_date', 'get_status']
    list_filter = ['assignment__course_offering__course__code']

    def get_status(self, obj):
        if obj.submitted:
            if obj.submit_date <= obj.assignment.deadline:
                return "Submitted"
            else:
                return "Late submission"
        else:
            return "Not submitted"
    get_status.short_description = "Status"

class AssignmentFileAdmin(GuardedModelAdmin):
    list_display = ['assignment', 'get_filename']
    list_filter = ['assignment__course_offering__term', 'assignment__course_offering__course__code']

    def get_filename(self, obj):
        return obj.filename()
    get_filename.short_description = "Reference material"


class AssignmentWorkFileAdmin(GuardedModelAdmin):
    list_display = ['get_assignment', 'get_student', 'get_filename']
    list_filter = ['assignment_work__assignment__course_offering__course__code']

    def get_filename(self, obj):              
        return obj.filename()
    get_filename.short_description = "Reference material"

    def get_assignment(self, obj):              
        return obj.assignment_work.assignment
    get_assignment.short_description = "Assignment"

    def get_student(self, obj):              
        return obj.assignment_work.student
    get_student.short_description = "Student"

admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(AssignmentWork, AssignmentWorkAdmin)
admin.site.register(AssignmentFile, AssignmentFileAdmin)
admin.site.register(AssignmentWorkFile, AssignmentWorkFileAdmin)
