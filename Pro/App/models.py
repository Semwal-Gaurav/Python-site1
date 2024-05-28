from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, default='profile_pics/OIP.jpeg')

    def __str__(self):
      return f'{self.user.username} Profile'
    

class ChatMessage(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)