from django.urls import include, path
from .views import ResultListView, ViewMyGrades, SelectedTerm

urlpatterns = [
    path('result/', include([
        path('', ResultListView.as_view(), name='result'),
        path('grades/', include([
            path('', ViewMyGrades.as_view(), name='my_grades'),
            path('<int:pk>/', SelectedTerm.as_view(), name='term'),
        ]))
    ]))
]

