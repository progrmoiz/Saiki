from django.contrib import admin
from .models import Announcement, AnnouncementFilter
from django.utils.html import format_html
from django.urls import reverse
from guardian.admin import GuardedModelAdmin

class AnnouncementAdmin(GuardedModelAdmin):
    readonly_fields = ('slug', 'created_at', 'updated_at')
    search_fields = ['title']
    list_filter = ['active', 'is_global', 'announcement_filters__program', 'announcement_filters__semester', 'announcement_filters__course']
    list_display = ["id", "get_announcement_filters", "created_by", "title", "start_date", "end_date", "is_global", "active"]

    def get_display_link(self, obj):
        return "<a href={}>{}</a>".format(
                    reverse('admin:{}_{}_change'.format(obj._meta.app_label, obj._meta.model_name), args=(obj.pk,)), 
                    obj.pk)

    def get_announcement_filters(self, obj):
        obj = obj.announcement_filters
        if obj:
            return format_html("<a href='{url}'>{title}</a>", url=reverse('admin:{}_{}_change'.format(obj._meta.app_label, obj._meta.model_name), args=(obj.pk,)), title=obj.pk)
        else:
            return None
    get_announcement_filters.short_description = 'AF ID'

    def get_changeform_initial_data(self, request):
        get_data = super(AnnouncementAdmin, self).get_changeform_initial_data(request)
        get_data['created_by'] = request.user.pk
        return get_data

class AnnouncementFilterAdmin(GuardedModelAdmin):
    search_fields = ['title']
    list_filter = ['program', 'semester', 'course']
    list_display = ["id", "title"]




admin.site.register(AnnouncementFilter, AnnouncementFilterAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
