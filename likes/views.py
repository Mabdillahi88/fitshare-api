from rest_framework import generics, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from profiles.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer

# List and create likes
class LikeList(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Check if the like already exists
        if Like.objects.filter(owner=self.request.user, post=serializer.validated_data['post']).exists():
            raise ValidationError("You have already liked this post.")
        serializer.save(owner=self.request.user)

# Retrieve and delete likes
class LikeDetail(generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
