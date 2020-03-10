# pages/urls.py
from django.urls import include, path

from .views import HomePageView, LoginView, LogoutView, AccountEditView, AccountView, ChangePasswordView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('accounts/', include([
        path('', AccountView.as_view(), name='profile'),
        path('edit/', AccountEditView.as_view(), name='edit_profile'),
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    ]))
]