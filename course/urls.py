from django.urls import include, path
from .views import CourseListView, CourseDetailView, CoursePeopleEditView, CourseHideFormView, CoursePeopleView
from assignment.urls import urlpatterns as assignment_urlpatterns

app_name = 'course'
urlpatterns = [
    path('', CourseListView.as_view(), name='index'),
    path('<str:slug>/', include([
        path('', CourseDetailView.as_view(), name='detail'),
        path('hide/<slug:pk>/', CourseHideFormView.as_view(), name='hide'),
        path('p/', CoursePeopleView.as_view(), name='people'),
        path('<int:username>', CoursePeopleEditView.as_view(), name='student'),
        path('w/', include('assignment.urls', namespace='assignment')),
        path('s/', include('stream.urls', namespace='stream')),
    ]))
]

