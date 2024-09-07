"""
URL configuration for AC project.

Crafted and Designed by Vcraftyu
"""
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.conf import settings
from Acapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Acapp.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)