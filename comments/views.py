from rest_framework import generics, permissions
from profiles.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]  # Add filter backend
    filterset_fields = ['post']  # Filter by the related post

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Retrieve, update, and delete comments
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
