from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('weather/', views.weather, name='weather'),
    path('submit/', views.submit_form, name='submit'),
]
