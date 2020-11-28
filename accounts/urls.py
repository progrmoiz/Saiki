# pages/urls.py
from django.urls import include, path

from .views import ForgetPasswordView, LoginView, LogoutView, AccountEditView, AccountView, ChangePasswordView

app_name = 'accounts'
urlpatterns = [
    path('', AccountView.as_view(), name='profile'),
    path('forget-password/', ForgetPasswordView.as_view(), name='forget'),
    path('edit/', AccountEditView.as_view(), name='edit'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change_pwd'),
]