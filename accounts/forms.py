from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    """Form para atualizar dados básicos do usuário"""
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }


class ProfileUpdateForm(forms.ModelForm):
    """Form para atualizar dados do perfil"""
    class Meta:
        model = Profile
        fields = ["name", "avatar", "bio"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nome de exibição"
            }),
            "bio": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Escreva algo sobre você"
            }),
            "avatar": forms.FileInput(attrs={"class": "form-control"}),
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    """Form para alteração de senha com labels em português"""
    old_password = forms.CharField(
        label="Senha atual",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    new_password1 = forms.CharField(
        label="Nova senha",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    new_password2 = forms.CharField(
        label="Confirme a nova senha",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
        }