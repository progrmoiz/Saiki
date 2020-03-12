# pages/urls.py
from django.urls import include, path

from .views import AnnouncementListView

urlpatterns = [
    path('announcement/', AnnouncementListView.as_view(), name='announcement'),
]