from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')
    followed = serializers.CharField(write_only=True)  # Accept either id or username as a string

    class Meta:
        model = Follower
        fields = ['id', 'owner', 'followed', 'followed_name', 'created_at']

    def validate_followed(self, value):
        """
        Validate the 'followed' field to accept both ID and username.
        """
        try:
            # Check if the value is a digit (indicating ID)
            if value.isdigit():
                return User.objects.get(id=value)
            # Otherwise, treat it as a username
            return User.objects.get(username=value)
        except User.DoesNotExist:
            raise ValidationError("The user you are trying to follow does not exist.")

    def create(self, validated_data):
        """
        Ensure the combination of 'owner' and 'followed' is unique.
        """
        owner = self.context['request'].user
        followed = validated_data['followed']

        if Follower.objects.filter(owner=owner, followed=followed).exists():
            raise ValidationError({'detail': 'You are already following this user.'})

        return Follower.objects.create(owner=owner, followed=followed)
