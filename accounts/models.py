from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=150, blank=True)  # nome de exibição opcional
    avatar = models.ImageField(upload_to="avatars/", default="avatars/default.jpg", blank=True, null=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # quando o perfil foi criado
    updated_at = models.DateTimeField(auto_now=True)      # última atualização

    def __str__(self):
        return self.name if self.name else f"Perfil de {self.user.username}"