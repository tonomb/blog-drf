from django.urls import path

from .views import ListComments, ListPosts, PostDetails, CommentsDetails


urlpatterns = [
    path("posts/", ListPosts.as_view()),
    path("posts/<int:pk>", PostDetails.as_view()),
    path("comments/", ListComments.as_view()),
    path("comments/<int:pk>", CommentsDetails.as_view()),
]
