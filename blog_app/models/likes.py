from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name="likes")
    create_date = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=False, default=False)
    object_id = models.PositiveIntegerField(null=True, blank=False, default=None)
    content_object = GenericForeignKey()

    class Meta:
        unique_together = [["user", "content_type", "object_id"]]
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
            models.Index(fields=["user"]),
            models.Index(fields=["create_date"]),
        ]
