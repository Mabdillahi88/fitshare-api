from rest_framework import serializers
from .models import Post
from likes.models import Like
from PIL import Image


class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title',
            'content', 'image', 'comments_count', 'likes_count',
            'is_owner', 'like_id'  # Removed 'profile_id' and 'profile_image'
        ]

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request and request.user == obj.owner

    def get_like_id(self, obj):
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

        # Use Pillow to open the image and check dimensions
        try:
            image = Image.open(value)
            if image.width > max_width or image.height > max_height:
                raise serializers.ValidationError("Image dimensions should not exceed 4096x4096 pixels.")
        except Exception as e:
            raise serializers.ValidationError("Invalid image file.")

        return value


# PostDetailSerializer for retrieving, updating, and deleting posts
class PostDetailSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = PostSerializer.Meta.fields
