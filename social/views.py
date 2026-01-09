from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from posts.models import Post
from posts.forms import PostForm
from .models import Follow, Like, Comment


@login_required
def feed(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("feed")
    else:
        form = PostForm()

    following_users = Follow.objects.filter(
        follower=request.user
    ).values_list("following", flat=True)

    posts = Post.objects.filter(
        author__in=list(following_users) + [request.user]
    ).order_by("-created_at")

    return render(
        request,
        "social/feed.html",
        {
            "form": form,
            "posts": posts,
        }
    )


@login_required
def follow_user(request, user_id):
    target = get_object_or_404(User, id=user_id)
    if target != request.user:
        Follow.objects.get_or_create(
            follower=request.user,
            following=target
        )
    return redirect("profile", username=target.username)


@login_required
def unfollow_user(request, user_id):
    target = get_object_or_404(User, id=user_id)
    Follow.objects.filter(
        follower=request.user,
        following=target
    ).delete()
    return redirect("profile", username=target.username)


@login_required
def like_toggle(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )
    if not created:
        like.delete()
    return redirect("feed")


@login_required
def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        text = request.POST.get("text", "").strip()
        if text:
            Comment.objects.create(
                user=request.user,
                post=post,
                text=text
            )
    return redirect("feed")