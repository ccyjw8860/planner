from rest_framework import serializers
from .models import Room
from users.models import User


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('title', 'description', 'host', 'participants', 'photo')