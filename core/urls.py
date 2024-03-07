from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skill/', views.skill, name='skill'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
