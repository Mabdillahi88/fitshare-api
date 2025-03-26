from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, Like, Comment
from achievements.models import Achievement

# Define thresholds for achievements
POPULAR_LIKES_THRESHOLD = 10
POPULAR_COMMENTS_THRESHOLD = 5
COMMENT_CHAMPION_THRESHOLD = 20

# Award "Popular Post" based on likes
@receiver(post_save, sender=Like)
def award_popular_post_by_like(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        if post.like_set.count() >= POPULAR_LIKES_THRESHOLD:
            # Check if the achievement has already been awarded for this user
            if not Achievement.objects.filter(user=post.owner, title="Popular Post").exists():
                Achievement.objects.create(
                    user=post.owner,
                    title="Popular Post",
                    description="One of your posts has received significant engagement through likes!"
                )

# Award "Popular Post" based on comments
@receiver(post_save, sender=Comment)
def award_popular_post_by_comment(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        if post.comment_set.count() >= POPULAR_COMMENTS_THRESHOLD:
            if not Achievement.objects.filter(user=post.owner, title="Popular Post").exists():
                Achievement.objects.create(
                    user=post.owner,
                    title="Popular Post",
                    description="One of your posts is trending with comments!"
                )

# Award "Comment Champion" for users who make many comments
@receiver(post_save, sender=Comment)
def award_comment_champion(sender, instance, created, **kwargs):
    if created:
        user = instance.owner
        # Count total comments made by the user
        comment_count = Comment.objects.filter(owner=user).count()
        if comment_count >= COMMENT_CHAMPION_THRESHOLD:
            if not Achievement.objects.filter(user=user, title="Comment Champion").exists():
                Achievement.objects.create(
                    user=user,
                    title="Comment Champion",
                    description="You have made 20 or more comments and are an active community member!"
                )
