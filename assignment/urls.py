from django.urls import include, path
from .views import AssignStudentPointView, AssignmentDeleteView, AssignmentEditUploadView, AssignmentListView, AssignmentDetailView, AssignmentCreateView, AssignmentEditView

app_name = 'assignment'
urlpatterns = [
    path('', AssignmentListView.as_view(), name='index'),
    path('create/', AssignmentCreateView.as_view(), name='create'),
    path('<uuid:slug>/', include([
        path('', AssignmentDetailView.as_view(), name='detail'),
        path('edit/', include([
            path('', AssignmentEditView.as_view(), name='edit'),
            path('upload/', AssignmentEditUploadView.as_view(), name='edit_upload'),
        ])),
        path('delete/', AssignmentDeleteView.as_view(), name='delete'),
        path('<int:username>', AssignStudentPointView.as_view(), name='assign_student_point'),
    ]))
]