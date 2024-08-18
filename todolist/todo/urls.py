from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.list_list,
        name='list_list'
    ),
    path(
        'create/',
        views.list_create,
        name='list_create'
    ),
    path(
        'delete/<int:list_id>/',
        views.list_delete,
        name='list_delete'
    ),
    path(
        '<int:list_id>/',
        views.task_list,
        name='task_list'
    ),
    path(
        '<int:list_id>/create/',
        views.task_create,
        name='task_create'
    ),
    path(
        '<int:list_id>/update/<int:pk>/',
        views.task_update,
        name='task_update'
    ),
    path(
        '<int:list_id>/delete/<int:pk>/',
        views.task_delete,
        name='task_delete'
    ),
]
