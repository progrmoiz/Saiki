from django.contrib import admin
from .models import Announcement, AnnouncementFilter
from django.utils.html import mark_safe
from django.urls import reverse

# Register your models here.

class AnnouncementAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['announcement_filters__department', 'announcement_filters__course', 'announcement_filters__semesters']
    list_display = ["title", "created_by", "start_date", "end_date", "is_global", "is_draft", "get_announcement_filters"]

    def get_display_link(self, obj):
        return "<a href={}>{}</a>".format(
                    reverse('admin:{}_{}_change'.format(obj._meta.app_label, obj._meta.model_name), args=(obj.pk,)), 
                    obj.pk)

    def get_announcement_filters(self, obj):
        return mark_safe(", ".join([self.get_display_link(p) for p in obj.announcement_filters.all()]))
    get_announcement_filters.short_description = 'Announcement Filter ID'

    def get_changeform_initial_data(self, request):
        get_data = super(AnnouncementAdmin, self).get_changeform_initial_data(request)
        get_data['created_by'] = request.user.pk
        return get_data

class AnnouncementFilterAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['department', 'course', 'semesters']
    list_display = ["id", "title", "get_departments", "get_courses", "semesters"]


admin.site.register(AnnouncementFilter, AnnouncementFilterAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
