from rest_framework import serializers
from .models import Post, Comment


class CommentSerialier(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "content", "author", "created_at")


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerialier(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "author",
            "comments",
            "created_at",
            "updated_at",
        )
