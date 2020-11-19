from django.contrib import admin
from .models import University, Department, Term, Program

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["code", "description"]

class ProgramAdmin(admin.ModelAdmin):
    list_display = ["code", "description"]

class UniversityAdmin(admin.ModelAdmin):
    list_display = ["name"]

class TermAdmin(admin.ModelAdmin):
    pass


admin.site.register(University, UniversityAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Term, TermAdmin)