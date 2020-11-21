from django.urls import include, path
from .views import CourseListView, CourseDetailView, CourseStudentRecordView, CourseHideFormView
from assignment.urls import urlpatterns as assignment_urlpatterns

app_name = 'course'
urlpatterns = [
    path('', CourseListView.as_view(), name='index'),
    path('<str:slug>/', include([
        path('', CourseDetailView.as_view(), name='detail'),
        path('hide/<slug:pk>/', CourseHideFormView.as_view(), name='hide'),
        path('<int:username>', CourseStudentRecordView.as_view(), name='student'),
        path('assignment/', include('assignment.urls', namespace='assignment')),
    ]))
]

