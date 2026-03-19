from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.SerializerMethodField()

    def get_profile_image(self, obj):
        """Safely return profile image URL."""
        try:
            if obj.profile.image:
                return obj.profile.image.url
        except (AttributeError, ValueError):
            pass
        return None

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image',
        )
