from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import NotFound


from .serializers import CommentSerialier, PostSerializer
from .models import Comment, Post


class ListPosts(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ListComments(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerialier


class CommentsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerialier


class ListCreateComments(generics.ListCreateAPIView):
    serializer_class = CommentSerialier

    def get_queryset(self):
        post_id = self.kwargs["post_id"]
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise NotFound("Post not found")
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        post_id = self.kwargs["post_id"]
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise NotFound("Post not found")
        serializer.save(post=post)


class ListDetailComments(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerialier

    def get_queryset(self):
        post_id = self.kwargs["post_id"]

        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise NotFound("Post Not found")
        return Comment.objects.filter(post=post)
