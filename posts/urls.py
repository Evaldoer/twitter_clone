from django.urls import path

from posts.api import posts_api
from .views import feed

urlpatterns = [
    path('feed/', feed, name='feed'),
    path("api/posts/", posts_api),
]
