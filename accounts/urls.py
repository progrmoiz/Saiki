# pages/urls.py
from django.urls import include, path

from .views import HomePageView, ForgetPasswordView, LoginView, LogoutView, AccountEditView, AccountView, ChangePasswordView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('accounts/', include([
        path('', AccountView.as_view(), name='profile'),
        path('forget_password/', ForgetPasswordView.as_view(), name='forget_password'),
        path('edit/', AccountEditView.as_view(), name='edit_profile'),
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    ]))
]