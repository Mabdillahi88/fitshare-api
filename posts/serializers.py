from rest_framework import serializers
from .models import Post
from PIL import Image

# Post Serializer for listing and creating posts
class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    image_filter = serializers.ChoiceField(choices=[
        ('_1977', '1977'), ('brannan', 'Brannan'), ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'), ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), ('normal', 'Normal'), ('nashville', 'Nashville'),
        ('rise', 'Rise'), ('toaster', 'Toaster'), ('valencia', 'Valencia'),
        ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ], default='normal')

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title',
            'content', 'image', 'image_filter', 'is_owner',
            'profile_id', 'profile_image'
        ]

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request and request.user == obj.owner

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
