from rest_framework import generics, permissions, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.annotate(
        comments_count=Count('comments', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['comments_count', 'likes_count', 'likes__created_at']
    search_fields = ['owner__username', 'title']
    filterset_fields = [
        'owner__profile',  # Posts created by a specific profile
        'likes__owner__profile',  # Posts liked by a specific profile
    ]

    def filter_queryset(self, queryset):
        """
        Adds additional filtering for posts created by profiles
        followed by a specific profile (profile_following query parameter).
        """
        queryset = super().filter_queryset(queryset)
        profile_id = self.request.query_params.get('profile_following')
        if profile_id:
            queryset = queryset.filter(
                owner__profile__followers__owner__profile=profile_id
            )
        return queryset

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.annotate(
        comments_count=Count('comments', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
