from django.contrib import admin
from .models import University, Department

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["code", "description"]

class UniversityAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(University, UniversityAdmin)
admin.site.register(Department, DepartmentAdmin)