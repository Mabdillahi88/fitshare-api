from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet

router = DefaultRouter()
# Register with an empty prefix so that the endpoint becomes /notifications/
router.register(r'', NotificationViewSet, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]
