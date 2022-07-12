from django.utils import timezone
from rest_framework import generics, permissions
from todo.models import Todo
from .serializers import TodosSerializer, CompleteTodoSerializer

class CompletedTodosListView(generics.ListAPIView):
    serializer_class = TodosSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user,datecompleted__isnull=False)
    
class CurrentTodosListCreateView(generics.ListCreateAPIView):
    serializer_class = TodosSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user,datecompleted__isnull=True)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class TodoUpdateRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodosSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    
class CompleteTodos(generics.UpdateAPIView):
    serializer_class = CompleteTodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    
    def perform_update(self,serializer):
        serializer.instance.datecompleted = timezone.now()
        serializer.save()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
