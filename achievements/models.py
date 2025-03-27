from django.db import models
from django.contrib.auth.models import User

class Achievement(models.Model):
    ACHIEVEMENT_CHOICES = [
        ('NEWBIE', 'Newbie'),
        ('POPULAR_POST', 'Popular Post'),
        ('COMMENT_CHAMPION', 'Comment Champion'),
        # Add more achievements here as needed
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=50,
        choices=ACHIEVEMENT_CHOICES,
        default='NEWBIE'
    )
    description = models.TextField(blank=True)
    date_earned = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_title_display()} - {self.user.username}"
