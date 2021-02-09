from rest_framework import serializers
from .models import User
from todos.models import Todo

class TodoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'start_date','end_date','is_success',)

class UserSerializer(serializers.ModelSerializer):
    todo = TodoUserSerializer(many=True)
    class Meta:
        model = User
        ordering = ['pk']
        fields =('pk','email', 'todo')