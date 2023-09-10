from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('weather/', views.weather, name='weather'),
    path('transportation-request/', views.transportation_request, name='transportation-request'),
    path('transportation-home/', views.transportation_home, name='transportation-home'),
    path('transportation-data/', views.transportation_data, name='transportation-data'),
    path('services/', views.services, name='services'),
    
]
