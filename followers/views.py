from rest_framework import generics, permissions
from .models import Follower
from .serializers import FollowerSerializer
from fitshare_api.permissions import IsOwnerOrReadOnly

class FollowerList(generics.ListCreateAPIView):
    """
    A class for FollowerList
    """
    serializer_class = FollowerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
        ]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    A class for FollowerDetail
    User to be able to retrieve a follower or unfollow user
    """
    serializer_class = FollowerSerializer
    permission_classes = [
        IsOwnerOrReadOnly
        ]
    queryset = Follower.objects.all()