from django.db import models
from users.models import User

class Room(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    host = models.ForeignKey(User, related_name='room_host', on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='room_participants', blank=True)
    photo = models.ImageField(upload_to='room_photos')
    photo_caption = models.CharField(max_length=500)

    def __str__(self):
        return self.title

