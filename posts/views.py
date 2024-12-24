from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer
from profiles.permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):
    """
    List posts or create a new post if logged in.
    The perform_create method associates the post with the logged-in user.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',  # Posts from followed profiles
        'likes__owner__profile',            # Posts liked by a specific user
        'owner__profile',                   # Posts owned by a specific user
        'category',                         # Posts filtered by category
    ]
    search_fields = [
        'owner__username',
        'title',
        'category',                         # Search by category
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',                # Order by likes creation time
    ]

    def perform_create(self, serializer):
        """
        Associate the post with the logged-in user.
        """
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a post.
    Updates and deletions are allowed only for the post owner.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
