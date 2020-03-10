from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Student, User, Guardian, PrevAcademicRecord

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
    list_display = ['user', 'full_name', 'email', 'gender', 'phone_number', 'CNIC']
    list_filter = ['gender']


    def full_name(self, obj):
        return "{} {}".format(obj.user.first_name, obj.user.last_name)

    full_name.short_description = 'Full Name'
    full_name.admin_order_field = 'user__first_name'

    def email(self, obj):
        return obj.user.email

    email.short_description = 'Email'
    email.admin_order_field = 'user__email'

class GuardianAdmin(admin.ModelAdmin):
    list_display = ["guardian_name", "CNIC", "phone_number", "relationship", "occupation"]

class PrevAcademicRecordAdmin(admin.ModelAdmin):
    list_display = ["college_name","year","start_date","end_date","percentage"]


admin.site.register(User, CustomUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(PrevAcademicRecord, PrevAcademicRecordAdmin)
admin.site.register(Guardian, GuardianAdmin)