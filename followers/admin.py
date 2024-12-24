from django.contrib import admin
from .models import Follower

@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'followed', 'created_at')  # Display follower details
    search_fields = ('owner__username', 'followed__username')  # Search by username
    list_filter = ('created_at',)  # Filter by creation date
    ordering = ('-created_at',)  # Order by newest followers first
