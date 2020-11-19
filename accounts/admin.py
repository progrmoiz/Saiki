from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm, EnrollmentActionForm
from .models import Student, User, Guardian, PrevAcademicRecord, Teacher
from course.models import CourseEnrollment, CourseOffering
from django.contrib import messages

def enroll_student(modeladmin, request, queryset):
    course = request.POST['course']
    course_offered = CourseOffering.objects.only('id').get(id=course)

    for student in queryset:
        student = Student.objects.only('user').get(user__id=student.user.id)
        CourseEnrollment.objects.get_or_create(
            course_offered=course_offered,
            student=student
        )
    messages.success(request,'Successfully enrolled {} students'.format(queryset.count()))
enroll_student.short_description = 'Enroll students to course'

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    prepopulated_fields = {'username': ('first_name' , 'last_name', )}

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_student', 'is_teacher')}),
    )

    list_filter = UserAdmin.list_filter + (
        'is_student', 'is_teacher'
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1', 'password2', 'is_student', 'is_teacher'),
        }),
    )


class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'display_name', 'email', 'program', 'semester', 'phone_number', 'CNIC']
    list_filter = ['gender', 'program', 'semester']
    search_fields = ['display_name', 'user__username', 'user__email', 'user__first_name', 'user__last_name']

    action_form = EnrollmentActionForm
    actions = [enroll_student]

    def email(self, obj):
        return obj.user.email

    email.short_description = 'Email'
    email.admin_order_field = 'user__email'

    class Media:
        #this path may be any you want, 
        #just put it in your static folder
        js = ('admin/js/enrollment.js', )
        css = {
            'all': ('admin/css/enrollment.css', )
        }

class GuardianAdmin(admin.ModelAdmin):
    list_display = ["guardian_name", "CNIC", "phone_number", "relationship", "occupation"]

class PrevAcademicRecordAdmin(admin.ModelAdmin):
    list_display = ["college_name","year","start_date","end_date","percentage"]

class TeacherAdmin(admin.ModelAdmin):
    list_display = ["user", "display_name", "gender", "title", "department"]
    list_filter = ['gender', 'department', 'title']
    search_fields = ['display_name', 'user__username', 'user__email', 'user__first_name', 'user__last_name']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(PrevAcademicRecord, PrevAcademicRecordAdmin)
admin.site.register(Guardian, GuardianAdmin)