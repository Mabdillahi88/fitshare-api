from rest_framework import generics, permissions
from .models import Follower
from .serializers import FollowerSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user or request.method in permissions.SAFE_METHODS

class FollowerList(generics.ListCreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class FollowerDetail(generics.RetrieveDestroyAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
