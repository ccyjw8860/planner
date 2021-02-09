from rest_framework import serializers
from .models import Todo, TodoPhoto

class TodoPhotoSeirializer(serializers.ModelSerializer):
    class Meta:
        model = TodoPhoto
        fields = ('caption', 'file')

class TodoSerializer(serializers.ModelSerializer):
    todo_photos = TodoPhotoSeirializer(many=True)
    class Meta:
        model = Todo
        fields = ('user', 'room','title','description','start_date','end_date','is_success','todo_photos')
