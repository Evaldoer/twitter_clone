from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "bio"]


class OptionalPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Senha atual",
        widget=forms.PasswordInput,
        required=False
    )
    new_password1 = forms.CharField(
        label="Nova senha",
        widget=forms.PasswordInput,
        required=False
    )
    new_password2 = forms.CharField(
        label="Confirme a nova senha",
        widget=forms.PasswordInput,
        required=False
    )