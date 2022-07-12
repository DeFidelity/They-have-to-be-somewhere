from django.urls import path 
from . import views
urlpatterns = [
    path('todos/completed/',views.CompletedTodosListView.as_view(),name='completed'),
    path('todos/', views.CurrentTodosListCreateView.as_view(), name='todos')
]