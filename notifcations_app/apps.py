from django.apps import AppConfig


class NotifcationsAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "notifcations_app"

    def ready(self):
        from . import signals
