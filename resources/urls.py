from django.urls import include, path

from .views import ResourceDetailView

app_name = 'resources'
urlpatterns = [
    path('', ResourceDetailView.as_view(), name='index'),
]

