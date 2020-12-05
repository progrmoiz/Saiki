from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import ResourceFolder, ResourceFile

# Register your models here.

class ResourceFolderAdmin(GuardedModelAdmin):
    readonly_fields = ('slug', )

class ResourceFileAdmin(GuardedModelAdmin):
    readonly_fields = ('slug', )

admin.site.register(ResourceFile, ResourceFileAdmin)
admin.site.register(ResourceFolder, ResourceFolderAdmin)