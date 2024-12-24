from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'created_at', 'updated_at')  # Display post details
    search_fields = ('title', 'owner__username', 'content')  # Search by title, username, or content
    list_filter = ('created_at', 'updated_at')  # Filter by creation or update date
    ordering = ('-created_at',)  # Order by newest posts first
