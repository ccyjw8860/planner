from rest_framework.generics import ListAPIView
from .models import User
from .serializer import UserSerializer

class UserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Create your views here.
