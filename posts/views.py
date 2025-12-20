from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

# Create your views here.


@login_required
def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/feed.html', {'posts': posts})
