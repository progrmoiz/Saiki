from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import ResourceFolder, ResourceFile

# Register your models here.

class ResourceFolderAdmin(GuardedModelAdmin):
    list_display = ["pk", "name", "course_offering", "parent", "created", "modified"]
    readonly_fields = ('slug', 'created', 'modified')
    list_filter = ['course_offering']

class ResourceFileAdmin(GuardedModelAdmin):
    list_display = ["pk", "name", "folder", "created", "modified"]
    readonly_fields = ('slug', 'name', 'created', 'modified')
    list_filter = ['folder__course_offering']

admin.site.register(ResourceFile, ResourceFileAdmin)
admin.site.register(ResourceFolder, ResourceFolderAdmin)