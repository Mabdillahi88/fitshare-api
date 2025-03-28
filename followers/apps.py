from django.apps import AppConfig

class FollowersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'followers'

    def ready(self):
        import followers.signals
