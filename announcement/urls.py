# pages/urls.py
from django.urls import include, path

from .views import AnnouncementListView, AnnouncementDetailView

app_name = 'announcement'
urlpatterns = [
    path('', AnnouncementListView.as_view(), name='index'),
    path('<int:pk>/', AnnouncementDetailView.as_view(), name='detail'),
]
