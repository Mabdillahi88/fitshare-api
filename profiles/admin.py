from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name', 'created_at', 'updated_at')  # Display profile details
    search_fields = ('owner__username', 'name', 'content')  # Search by username, name, or content
    list_filter = ('created_at', 'updated_at')  # Filter by creation or update date
    ordering = ('-created_at',)  # Order by newest profiles first
