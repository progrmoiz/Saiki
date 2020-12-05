from django.urls import include, path
from .views import ResourceFileList, ResourceFolderDestroy, ResourceFileDestroy, ResourceFolderCreate, ResourceFileCreate

app_name = 'resources'
urlpatterns = [
    path("resources/<str:folder_slug>/", ResourceFileList.as_view(), name="folder_list"),
    path("resources/d/create/", ResourceFolderCreate.as_view(), name="folder_create"),
    path("resources/f/create/", ResourceFileCreate.as_view(), name="file_create"),
    path("resources/d/<int:pk>/", ResourceFolderDestroy.as_view(), name="folder_detail"),
    path("resources/f/<int:pk>/", ResourceFileDestroy.as_view(), name="file_detail"),
]

