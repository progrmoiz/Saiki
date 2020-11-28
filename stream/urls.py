from django.urls import include, path

from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView

app_name = 'stream'
urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('create/', PostCreateView.as_view(), name='create-post'),
    path('<str:post_slug>/', include([
        path('', PostDetailView.as_view(), name='post-detail'),
        path('delete/', PostDeleteView.as_view(), name='delete-post'),
    ])),
]

