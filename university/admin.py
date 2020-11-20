from django.contrib import admin
from .models import University, Department, Term, Program
from guardian.admin import GuardedModelAdmin

# Register your models here.

class DepartmentAdmin(GuardedModelAdmin):
    list_display = ["code", "description"]

class ProgramAdmin(GuardedModelAdmin):
    list_display = ["code", "description"]

class UniversityAdmin(GuardedModelAdmin):
    list_display = ["name"]

class TermAdmin(GuardedModelAdmin):
    pass


admin.site.register(University, UniversityAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Term, TermAdmin)