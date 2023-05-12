from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('about/', views.about, name='about' ),
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('pkgs/', views.pkgs, name='pkg'),
]