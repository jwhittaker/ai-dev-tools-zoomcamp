from django.urls import path
from .views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoCompleteView

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-list'),
    path('create/', TodoCreateView.as_view(), name='todo-create'),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='todo-update'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='todo-delete'),
    path('complete/<int:pk>/', TodoCompleteView.as_view(), name='todo-complete'),
]
