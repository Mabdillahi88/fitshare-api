from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from followers.models import Follower
from notifications.models import Notification

# Notify when a user is followed
@receiver(post_save, sender=Follower)
def notify_follow(sender, instance, created, **kwargs):
    if created:
        # Only notify if the follower is not following themselves
        if instance.owner != instance.followed:
            Notification.objects.create(
                recipient=instance.followed,
                message=f"{instance.owner.username} started following you."
            )

# Notify when a user is unfollowed
@receiver(pre_delete, sender=Follower)
def notify_unfollow(sender, instance, **kwargs):
    # Optionally, create a notification for an unfollow event.
    Notification.objects.create(
        recipient=instance.followed,
        message=f"{instance.owner.username} unfollowed you."
    )
