from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer
from .permissions import IsOwnerOrReadOnly

# List all profiles
class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]

# Retrieve, update, and delete a profile
class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
