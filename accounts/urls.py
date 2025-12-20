from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile, edit_profile

urlpatterns = [
    # Autenticação
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="login"),
        name="logout"
    ),

    # Cadastro
    path("register/", register, name="register"),

    # Perfil
    path("profile/", profile, name="profile"),
    path("edit_profile/", edit_profile, name="edit_profile"),
]
