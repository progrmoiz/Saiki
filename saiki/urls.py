"""saiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from accounts.views import HomePageView
from django.views.i18n import JavaScriptCatalog
from rest_framework import routers

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('api/', include('course.api.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('c/', include('course.urls', namespace='course')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('announcement/', include('announcement.urls', namespace='announcement')),
    path(r'comments/', include('django_comments_xtd.urls')),
    path(r'jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('r/', include('result.urls', namespace='result')),
    path('w/', include('assignment.urls', namespace='assignment')),
    path('admin/', admin.site.urls),
    path('avatar/', include('avatar.urls')),
    url('^inbox/notifications/', include('notifications.urls', namespace='notifications')),
]

admin.site.site_header = "Saiki Administration"
admin.site.site_title = "Saiki Administration Portal"
admin.site.index_title = "Welcome to Saiki Administration Portal"

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
