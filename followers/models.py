from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model to define the relationship between users.
    - 'owner': The User who is following another user.
    - 'followed': The User being followed by the 'owner'.
    """

    # The user who is following another user
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    # The user being followed by the owner
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    # Timestamp of when the follow relationship was created
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta options for the Follower model:
        - Order follow relationships by creation date (newest first).
        - Ensure that a user cannot follow the same user multiple times.
        """
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        """
        String representation of the Follower instance.
        Example: "owner_username follows followed_username".
        """
        return f'{self.owner.username} follows {self.followed.username}'
