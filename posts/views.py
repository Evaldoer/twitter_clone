from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm
from social.models import Follow


@login_required
def feed(request):
    # =========================
    # Criar novo post
    # =========================
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("feed")
    else:
        form = PostForm()

    # =========================
    # Usuários que eu sigo
    # =========================
    following_users = Follow.objects.filter(
        follower=request.user
    ).values_list("following", flat=True)

    # =========================
    # Posts do feed:
    # - meus posts
    # - posts de quem sigo
    # =========================
    posts = Post.objects.filter(
        author__in=list(following_users) + [request.user]
    ).order_by("-created_at")

    return render(
        request,
        "posts/feed.html",
        {
            "posts": posts,
            "form": form,
        }
    )