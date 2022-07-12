from django.urls import path 
from . import views
urlpatterns = [
    path('todos/completed/',views.CompletedTodosListView.as_view(),name='completed'),
    path('todos/', views.CurrentTodosListCreateView.as_view(), name='todos'),
    path('todos/<int:pk>/',views.TodoUpdateRetrieveDestroyView.as_view(),name='todo_update'),
    path('todos/<int:pk>/complete',views.CompleteTodos.as_view(), name='complete_todos')
]