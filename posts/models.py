from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images/', blank=True)

    def __str__(self):
        return self.title
