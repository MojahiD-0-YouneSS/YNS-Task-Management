from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_task, name='add_task'),
    path('', views.view_tasks, name='view_tasks'),
    path('mark/<int:task_id>/', views.mark_task_as_complete, name='mark_task_as_complete'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('search/', views.search_tasks, name='search_tasks'),
]

