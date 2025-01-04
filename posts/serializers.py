from rest_framework import serializers
from .models import Post
from likes.models import Like
from PIL import Image


class PostSerializer(serializers.ModelSerializer):
    # Read-only fields for additional information
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title',
            'content', 'image', 'image_filter', 'category',
            'comments_count', 'likes_count', 'is_owner', 'like_id'
        ]
        read_only_fields = ['owner', 'comments_count', 'likes_count', 'is_owner', 'like_id']

    def get_is_owner(self, obj):
        """
        Determines if the currently logged-in user is the owner of the post.
        """
        request = self.context.get('request')
        return request and request.user == obj.owner

    def get_like_id(self, obj):
        """
        Gets the ID of the like object associated with the post and the current user.
        """
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            like = Like.objects.filter(owner=request.user, post=obj).first()
            return like.id if like else None
        return None

    def validate_image(self, value):
        """
        Validates the uploaded image size, width, and height.
        """
        max_size = 2 * 1024 * 1024  # 2MB
        max_width = 4096
        max_height = 4096

        # Check file size
        if value.size > max_size:
            raise serializers.ValidationError("Image file too large. Size should not exceed 2 MB.")

        # Check image dimensions using Pillow
        try:
            image = Image.open(value)
            if image.width > max_width or image.height > max_height:
                raise serializers.ValidationError("Image dimensions should not exceed 4096x4096 pixels.")
        except Exception:
            raise serializers.ValidationError("Invalid image file.")

        return value

    def create(self, validated_data):
        """
        Override the create method to handle any necessary custom logic
        and ensure no non-model fields are passed to `Post.objects.create`.
        """
        # Remove read-only fields that may inadvertently be passed
        validated_data.pop('comments_count', None)
        validated_data.pop('likes_count', None)
        validated_data.pop('is_owner', None)
        validated_data.pop('like_id', None)

        # Create and return the post instance
        return Post.objects.create(**validated_data)
