from rest_framework.generics import ListAPIView
from .models import Room
from .serializers import RoomSerializer

class RoomView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

# Create your views here.
