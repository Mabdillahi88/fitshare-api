from django.contrib import admin
from .models import Achievement

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'date_earned')
    list_filter = ('title', 'date_earned')
    search_fields = ('user__username', 'title')

admin.site.register(Achievement, AchievementAdmin)
