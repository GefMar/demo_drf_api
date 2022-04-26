from django.db import models

from .choices import OperationSystemChoice

__all__ = ("Notification",)


class Notification(models.Model):
    notification_text = models.TextField(blank=False, null=False)
    operation_system = models.CharField(
        max_length=24, choices=OperationSystemChoice.choices, default=OperationSystemChoice.ANY, null=False,
    )
