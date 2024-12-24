from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from profiles.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer

class LikeList(generics.ListCreateAPIView):
    """
    List all likes or create a new like.
    Prevents duplicate likes.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """
        Prevent duplicate likes by the same user on the same post.
        """
        if Like.objects.filter(owner=self.request.user, post=serializer.validated_data['post']).exists():
            raise ValidationError("You have already liked this post.")
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or delete a like.
    Deletion is restricted to the owner.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
