from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('add/', views.add_project, name='add_project'),
    path('update/<int:id>/', views.update_project, name='update_project'),
    path('delete/<int:id>/', views.delete_project, name='delete_project'),
]
