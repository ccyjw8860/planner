from django.db import models
from users.models import User
from rooms.models import Room

class Todo(models.Model):
    user = models.ForeignKey(User, related_name='todo', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='todo', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def is_success(self):
        if len(self.todo_photos.all()) > 0:
            return True
        else:
            return False

    def __str__(self):
        return self.title

class TodoPhoto(models.Model):
    caption = models.CharField(max_length=100)
    file = models.ImageField(upload_to='todo_photos')
    todo = models.ForeignKey(Todo, related_name='todo_photos', on_delete=models.CASCADE)

    def __str__(self):
        return self.caption