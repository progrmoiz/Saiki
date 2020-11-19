from django.urls import include, path
from .views import CourseListView, CourseDetailView, CourseStudentRecordView
from assignment.urls import urlpatterns as assignment_urlpatterns

urlpatterns = [
    path('course/', include([
        path('', CourseListView.as_view(), name='course'),
        path('<str:slug>/', include([
            path('', CourseDetailView.as_view(), name='course_detail'),
            path('<int:username>', CourseStudentRecordView.as_view(), name='course_student_student'),
            *assignment_urlpatterns
        ]))
    ]))
]

