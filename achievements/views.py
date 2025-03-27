from rest_framework import viewsets
from .models import Achievement
from .serializers import AchievementSerializer
from rest_framework.permissions import IsAuthenticated

class AchievementViewSet(viewsets.ModelViewSet):
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Achievement.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
