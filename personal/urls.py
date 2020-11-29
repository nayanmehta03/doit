from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='personal-home'),
    path('add-board/', views.add_board, name='add_board'),
    path('tasks/<board_id>/', views.tasks, name='tasks'),
    path('tasks/<board_id>/add_task/', views.add_task, name='add-task'),
    path('delete_task/<task_id>', views.delete_task, name='delete-task'),
    path('start_task/<task_id>', views.start_task, name='start-task'),
    path('complete_task/<task_id>/', views.complete_task, name='complete-task'),
    path('delete_board/<board_id>', views.delete_board, name='delete-board'),
]
