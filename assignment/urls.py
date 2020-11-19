from django.urls import include, path
from .views import AssignStudentPointView, AssignmentDeleteView, AssignmentEditUploadView, AssignmentListView, AssignmentDetailView, AssignmentCreateView, AssignmentEditView

urlpatterns = [
    path('assignment/', include([
        path('', AssignmentListView.as_view(), name='assignment'),
        path('create/', AssignmentCreateView.as_view(), name='assignment_create'),
        path('<uuid:slug>/', include([
            path('', AssignmentDetailView.as_view(), name='assignment_detail'),
            path('edit/', include([
                path('', AssignmentEditView.as_view(), name='assignment_edit'),
                path('upload/', AssignmentEditUploadView.as_view(), name='assignment_edit_upload'),
            ])),
            path('delete/', AssignmentDeleteView.as_view(), name='assignment_delete'),
            path('<int:username>', AssignStudentPointView.as_view(), name='assign_student_point'),
        ]))
    ]))
]