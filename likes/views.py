from rest_framework import generics, permissions
from profiles.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer

# List and create likes
class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
