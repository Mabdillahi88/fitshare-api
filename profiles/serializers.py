from rest_framework import serializers
from django.db.models import Count
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()  # New field
    followers_count = serializers.ReadOnlyField()  # New field
    following_count = serializers.ReadOnlyField()  # New field

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name', 'content',
            'image', 'is_owner', 'following_id', 'posts_count',
            'followers_count', 'following_count'
        ]

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request and request.user == obj.owner

    def get_following_id(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            follower = Follower.objects.filter(owner=request.user, followed=obj.owner).first()
            return follower.id if follower else None
        return None
