from django.db import models
from django.db.models.signals import post_save
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
        return f"{self.owner.username}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Signal to automatically create a Profile for each new User.
    """
    if created:
        Profile.objects.create(owner=instance)


# Connect the signal to the User model
post_save.connect(create_profile, sender=User)
