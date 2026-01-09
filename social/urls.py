from django.urls import path
from . import views

urlpatterns = [
    # Seguir / deixar de seguir
    path("follow/<int:user_id>/", views.follow_user, name="follow_user"),
    path("unfollow/<int:user_id>/", views.unfollow_user, name="unfollow_user"),

    # Feed
    path("feed/", views.feed, name="feed"),

    # Curtidas
    path("like/<int:post_id>/", views.like_toggle, name="like_toggle"),

    # Comentários
    path("comment/<int:post_id>/", views.comment_create, name="comment_create"),
]