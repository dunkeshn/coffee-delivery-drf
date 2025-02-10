from rest_framework import serializers

from blog.models.post import Post
from users.models.profile import Profile


class LikedPostsShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            ('id', 'title', )
        )

class ProfileShortSerializer(serializers.ModelSerializer):
    liked_posts = LikedPostsShortSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = (
            'telegram_id',
            'beans',
            'author_status',
            'liked_posts',
        )


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'telegram_id',
        )
