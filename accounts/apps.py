from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
    verbose_name = "Gerenciamento de Contas"

    def ready(self):
        # importa os signals quando o app é carregado
        import accounts.signals