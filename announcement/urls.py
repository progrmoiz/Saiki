# pages/urls.py
from django.urls import include, path

from .views import AnnouncementListView, AnnouncementDetailView

urlpatterns = [
    path('announcement/', include([
        path('', AnnouncementListView.as_view(), name='announcement'),
        path('<int:pk>/', AnnouncementDetailView.as_view(), name='announcement_detail'),
    ]))
]
