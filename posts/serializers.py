# serializers.py
from rest_framework import serializers
from posts.models import Post, Image
from likes.models import Like

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    images = ImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        post = Post.objects.create(**validated_data)
        for image in uploaded_images:
            Image.objects.create(post=post, image=image)
        return post

    def validate_uploaded_images(self, images_data):
        for image_data in images_data:
            if image_data.size > 2 * 1024 * 1024:
                raise serializers.ValidationError('Image size larger than 2MB!')
            if image_data.image.height > 4096:
                raise serializers.ValidationError('Image height larger than 4096px!')
            if image_data.image.width > 4096:
                raise serializers.ValidationError('Image width larger than 4096px!')
        return images_data

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image_filter',
            'like_id', 'likes_count', 'comments_count', 'images', 'uploaded_images',
        ]
