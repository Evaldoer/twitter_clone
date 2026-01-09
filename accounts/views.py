from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm, CustomPasswordChangeForm
from social.models import Follow

# =========================
# Cadastro de usuário
# =========================
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("feed")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})

# =========================
# Visualização de perfil
# =========================
@login_required
def profile_detail(request, username):
    profile_user = get_object_or_404(User, username=username)

    is_following = False
    if request.user != profile_user:
        is_following = Follow.objects.filter(
            follower=request.user,
            following=profile_user
        ).exists()

    return render(request, "accounts/profile.html", {
        "profile_user": profile_user,
        "is_following": is_following,
    })

# =========================
# Edição de perfil
# =========================
@login_required
def profile_edit(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile", username=request.user.username)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, "accounts/edit_profile.html", {
        "user_form": user_form,
        "profile_form": profile_form,
    })

# =========================
# Busca de usuários
# =========================
@login_required
def user_search(request):
    query = request.GET.get("q", "").strip()
    users = User.objects.filter(username__icontains=query).exclude(id=request.user.id) if query else []
    return render(request, "accounts/user_search.html", {"users": users, "query": query})

# =========================
# Alteração de senha
# =========================
class UserPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("profile_edit")