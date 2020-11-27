from django.urls import include, path
from .views import AssignmentWorkDetail, AssignmentWorkFileList, AssignmentWorkFileDetail, AssignmentFileList, AssignmentFileDetail

app_name = 'assignment'
urlpatterns = [
    path("assignments/<int:assignment_pk>/materials/", AssignmentFileList.as_view(), name="assignment_file_list"),
    path("assignments/<int:assignment_pk>/materials/<int:material_pk>", AssignmentFileDetail.as_view(), name="assignment_file_detail"),
    
    path("assignmentworks/<int:assignmentwork_pk>/", AssignmentWorkDetail.as_view(), name="assignment_detail"),
    path("assignmentworks/<int:assignmentwork_pk>/work-materials/", AssignmentWorkFileList.as_view(), name="assignment_work_file_list"),
    path("assignmentworks/<int:assignmentwork_pk>/work-materials/<int:workmaterial_pk>", AssignmentWorkFileDetail.as_view(), name="assignment_work_file_detail"),
]

