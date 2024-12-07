from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Profile
from .serializers import ProfileSerializer
from profiles.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__followed__created_at',
        'owner__following__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

