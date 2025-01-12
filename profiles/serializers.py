from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    image_url = serializers.SerializerMethodField()  # Dynamic image URL field

    def get_image_url(self, obj):
        """
        Returns the Cloudinary URL for the default image or the URL of the uploaded image.
        """
        if obj.image.name == 'default_profile.jpg':
            # Return the Cloudinary-hosted default image
            return (
                'https://res.cloudinary.com/dffdb3kza/image/upload/v1736456577/default_profile_acp73s.jpg'
            )
        # Return the uploaded image's URL
        return obj.image.url

    def get_is_owner(self, obj):
        """
        Checks if the current user is the owner of the profile.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Returns the ID of the Follower relationship if the current user is following the profile owner.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'image_url', 'is_owner', 'following_id',
            'posts_count', 'followers_count', 'following_count',
        ]
