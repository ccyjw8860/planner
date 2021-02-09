from rest_framework.generics import ListAPIView
from .models import Todo
from .serializer import TodoSerializer

class TodoView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

