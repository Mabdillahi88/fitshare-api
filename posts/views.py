from rest_framework import generics, permissions, filters
from django.db.models import Count
from .models import Post
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend




class PostList(generics.ListAPIView):
    queryset = Post.objects.annotate(
        comments_count=Count('comments', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['comments_count', 'likes_count', 'likes__created_at']
    search_fields = ['owner__username', 'title']
    filterset_fields = [
        'owner__profile',  # Filter by posts owned by a user
        'likes__owner__profile',  # Filter by posts liked by a user
        'owner__profile__following__followed__profile',  # Filter by posts by users a profile follows
    ]




class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.annotate(
        comments_count=Count('comments', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


