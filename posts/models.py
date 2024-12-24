from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e., a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)  # Made optional
    image = models.ImageField(
        upload_to='images/', 
        default='../default_post_rgq6aq', 
        blank=True  # Added default and blank=True
    )
    image_filter = models.CharField(
        max_length=32,  # Reduced to match DRF
        choices=image_filter_choices, 
        default='normal'
    )
    category = models.CharField(max_length=100, blank=True)  # Added category field

    class Meta:
        ordering = ['-created_at']  # Ensures newest posts appear first

    def __str__(self):
        return f'{self.id} {self.title}'  # Provides better representation
