from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import Post

# Register your models here.

class PostAdmin(GuardedModelAdmin):
    readonly_fields = ('slug', 'publish', 'modified')

admin.site.register(Post, PostAdmin)
