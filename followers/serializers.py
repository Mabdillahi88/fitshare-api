from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')
    followed = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all(), write_only=True)

    class Meta:
        model = Follower
        fields = ['id', 'owner', 'followed', 'followed_name', 'created_at']

    def create(self, validated_data):
        owner = self.context['request'].user
        followed = validated_data['followed']

        if Follower.objects.filter(owner=owner, followed=followed).exists():
            raise ValidationError({'detail': 'You are already following this user.'})

        return Follower.objects.create(owner=owner, followed=followed)
