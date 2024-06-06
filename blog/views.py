from django.shortcuts import render
from rest_framework import generics


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
