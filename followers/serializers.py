from rest_framework import serializers
from django.db import IntegrityError
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = ['id', 'owner', 'followed', 'followed_name', 'created_at']

    def create(self, validated_data):
        """
        Handles IntegrityError when a duplicate Follower is created.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You are already following this user.'
            })
