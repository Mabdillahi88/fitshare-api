from rest_framework import serializers
from .models import Post

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

        if value.size > max_size:
            raise serializers.ValidationError("Image file too large. Size should not exceed 2 MB.")
        
        if value.width > max_width:
            raise serializers.ValidationError("Image width should not exceed 4096 pixels.")
        
        if value.height > max_height:
            raise serializers.ValidationError("Image height should not exceed 4096 pixels.")

        return value
