from rest_framework import viewsets
from .models import Achievement
from .serializers import AchievementSerializer
from rest_framework.permissions import IsAuthenticated

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
