# serializers.py

from rest_framework import serializers
from posts.models import Post, Image
from likes.models import Like

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']

class PostCreateSerializer(serializers.ModelSerializer):
    # Include the necessary logic for handling images during creation
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = [
            'title', 'content', 'images', 'image_filter',
        ]

    def create(self, validated_data):
        # Extract images data and create images separately
        images_data = validated_data.pop('images', [])
        post = Post.objects.create(**validated_data)

        for image_data in images_data:
            Image.objects.create(post=post, **image_data)

        return post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    images = ImageSerializer(many=True)  # Use the ImageSerializer for the images field

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError('Image height larger than 4096px!')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width larger than 4096px!')
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'images', 'image_filter',
            'like_id', 'likes_count', 'comments_count',
        ]
