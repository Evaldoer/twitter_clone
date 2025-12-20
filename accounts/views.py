from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import UserUpdateForm, ProfileUpdateForm


# Cadastro de usuário
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # login automático após cadastro
            return redirect("feed")
    else:
        form = UserCreationForm()

    return render(request, "accounts/register.html", {"form": form})


# Perfil do usuário (visualização e edição básica)
@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(
        request,
        "accounts/profile.html",  # 🔥 caminho completo
        {
            "user_form": user_form,
            "profile_form": profile_form
        }
    )


# Edição de perfil (separado em outra rota)
@login_required
def edit_profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")  # volta para a página de perfil

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(
        request,
        "accounts/edit_profile.html",  # 🔥 caminho completo
        {
            "user_form": user_form,
            "profile_form": profile_form
        }
    )