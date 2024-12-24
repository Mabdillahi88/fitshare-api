from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from profiles.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

class CommentList(generics.ListCreateAPIView):
    """
    List all comments or create a new comment.
    Allows filtering by post and owner.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'post',  # Filter comments for a specific post
        'owner', # Filter comments by a specific user
    ]

    def perform_create(self, serializer):
        """
        Associate the comment with the logged-in user.
        """
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a comment.
    Updates and deletions are restricted to the owner.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
