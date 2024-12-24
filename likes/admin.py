from django.contrib import admin
from .models import Like

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'post', 'created_at')  # Display like details
    search_fields = ('owner__username', 'post__title')  # Search by username or post title
    list_filter = ('created_at',)  # Filter by creation date
    ordering = ('-created_at',)  # Order by newest likes first
