from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='https://res.cloudinary.com/dffdb3kza/image/upload/v1721745890/default_profile_ninx4o.jpg',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Profile of {self.owner.username}"
