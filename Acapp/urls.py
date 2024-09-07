from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from . import views
from django.urls import reverse_lazy

urlpatterns = [
    path('',views.index, name='index'),
    path('service/',views.service, name='service'),
    path('gallery/',views.gallery, name='gallery'),
    path('latestprojects/',views.latestprojects, name='latestprojects'),
    path('collaboration/', views.collaboration, name='collaboration'),
    path('completedprojects/',views.completedprojects, name='completedprojects'),
    path('clothing/',views.clothing, name='clothing'),
    path('hilton/',views.hilton, name='hilton'),
    path('hyatt/',views.hyatt, name='hyatt'),
    path('contact/',views.contact, name='contact')
]
