from django.urls import path
from .views import ItemListView, ToDoListView, ToDoCreateView, ItemCreateView

urlpatterns = [
        path(
            'items/',
            ItemListView.as_view(),
            name='item_list'),
    path(
        'items/new/', 
        ItemCreateView.as_view(),
        name='item_create'),
    path(
        'items/<int:pk>/',
        ToDoListView.as_view(),
        name='todo_list'),
    path(
        'items/<int:pk>/new/',
        ToDoCreateView.as_view(),
        name='todo_create'),
]
