from django.contrib.auth import views as auth_views
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
    path(
        'update_task_status/<int:task_id>/',
        views.update_task_status,
        name='update_task_status'
    ),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        'signup/',
        views.signup,
        name='signup'
    ),
]
