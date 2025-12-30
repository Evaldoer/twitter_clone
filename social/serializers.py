from rest_framework import serializers
from .models import Comment
from posts.models import Post  # assumindo que seus posts estão no app "posts"


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "user", "text", "created_at")


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)
    author_name = serializers.CharField(source="author.profile.name", read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "author",
            "author_name",
            "content",
            "created_at",
            "comments",
            "likes_count",
        )