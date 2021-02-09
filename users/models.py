from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(null=False, blank=False, unique=True)
    nickname = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='user_photos')

    def __str__(self):
        return self.email