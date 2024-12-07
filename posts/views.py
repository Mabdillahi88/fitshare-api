from rest_framework import generics, permissions, filters
from django.db.models import Count
from .models import Post
from .serializers import PostSerializer



class PostList(generics.ListAPIView):
    queryset = Post.objects.annotate(
        comments_count=Count('comments', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['comments_count', 'likes_count', 'likes__created_at']
    search_fields = ['owner__username', 'title']  # Search by author's username or post title



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.annotate(
        comments_count=Count('comments', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

