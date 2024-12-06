from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    image_filter = models.CharField(
        max_length=50,
        choices=[
            ('_1977', '1977'), ('brannan', 'Brannan'), ('earlybird', 'Earlybird'),
            ('hudson', 'Hudson'), ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
            ('kelvin', 'Kelvin'), ('normal', 'Normal'), ('nashville', 'Nashville'),
            ('rise', 'Rise'), ('toaster', 'Toaster'), ('valencia', 'Valencia'),
            ('walden', 'Walden'), ('xpro2', 'X-pro II')
        ],
        default='normal'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
