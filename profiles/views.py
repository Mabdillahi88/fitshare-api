from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Profile
from .serializers import ProfileSerializer
from profiles.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['created_at']
    filterset_fields = [
        'owner__following__followed__profile',  # Profiles following a profile
    ]

class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
