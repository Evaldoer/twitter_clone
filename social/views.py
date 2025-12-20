from django.shortcuts import render

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Follow
# Create your views here.


@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    Follow.objects.get_or_create(
        follower=request.user,
        following=user_to_follow
    )
    return redirect('profile')


@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    Follow.objects.filter(
        follower=request.user,
        following=user_to_unfollow
    ).delete()
    return redirect('profile')

