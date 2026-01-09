from django.apps import AppConfig


class SocialConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "social"

    def ready(self):
        # importa os signals quando o app é carregado
        import social.signals