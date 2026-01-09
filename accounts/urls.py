from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    register, profile_detail, profile_edit,
    UserPasswordChangeView, user_search
)

urlpatterns = [
    # Autenticação
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    # Cadastro
    path("register/", register, name="register"),

    # Perfil
    path("profile/edit/", profile_edit, name="profile_edit"),
    path("profile/<str:username>/", profile_detail, name="profile"),

    # Busca
    path("search/", user_search, name="user_search"),

    # Alteração de senha
    path("password/change/", UserPasswordChangeView.as_view(), name="password_change"),
]