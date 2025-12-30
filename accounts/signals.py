from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Cria um Profile automaticamente quando um novo User é registrado"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """Garante que o Profile seja salvo quando o User for atualizado"""
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        # fallback: cria caso não exista
        Profile.objects.create(user=instance)