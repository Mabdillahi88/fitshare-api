from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'owner', 'content', 'created_at')  # Replaced 'body' with 'content'
    search_fields = ('owner__username', 'content')  # Search by username or comment content
    list_filter = ('created_at', 'post')  # Filter by creation date and post
    ordering = ('-created_at',)  # Order by newest comments first
