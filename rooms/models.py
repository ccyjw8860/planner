from django.db import models
from users.models import User

class Room(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    host = models.ForeignKey(User, related_name='host', on_delete=models.CASCADE)
    participants = models.ManyToManyField(User)

    def __str__(self):
        return self.title

class RoomPhoto(models.Model):
    caption = models.CharField(max_length=100)
    file = models.ImageField(upload_to='room_photos')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
