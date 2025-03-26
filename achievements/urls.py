from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AchievementViewSet

router = DefaultRouter()
# Register with an empty prefix so that the final route is simply /achievements/
router.register(r'', AchievementViewSet, basename='achievement')

urlpatterns = [
    path('', include(router.urls)),
]
