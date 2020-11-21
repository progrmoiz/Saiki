from django.urls import include, path
from .views import ResultListView, ViewMyGrades, SelectedTerm

app_name = 'result'
urlpatterns = [
    path('', ResultListView.as_view(), name='index'),
    path('terms/', include([
        path('', ViewMyGrades.as_view(), name='select_term'),
        path('<int:pk>/', SelectedTerm.as_view(), name='by_term'),
    ]))
]

