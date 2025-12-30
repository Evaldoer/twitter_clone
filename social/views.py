from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

from .models import Follow, Like, Comment
from posts.models import Post  # assumindo que seus posts estão em app "posts"


# Seguir usuário
@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if user_to_follow != request.user:
        Follow.objects.get_or_create(
            follower=request.user,
            following=user_to_follow
        )
    return redirect("profile", username=user_to_follow.username)


# Deixar de seguir usuário
@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    Follow.objects.filter(
        follower=request.user,
        following=user_to_unfollow
    ).delete()
    return redirect("profile", username=user_to_unfollow.username)


# Feed de posts (apenas dos seguidos)
@login_required
def feed(request):
    following_users = Follow.objects.filter(
        follower=request.user
    ).values_list("following_id", flat=True)

    posts = Post.objects.filter(
        author_id__in=following_users
    ).select_related("author").prefetch_related("likes", "comments").order_by("-created_at")

    return render(request, "social/feed.html", {"posts": posts})


# Curtir/Descurtir post
@login_required
@require_POST
def like_toggle(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect("feed")


# Criar comentário
@login_required
@require_POST
def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    text = request.POST.get("text", "").strip()
    if text:
        Comment.objects.create(user=request.user, post=post, text=text)
    return redirect("feed")