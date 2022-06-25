from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .likes import Like


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name="comments")
    create_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=False, blank=False)
    likes = GenericRelation(Like)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=False, default=None)
    object_id = models.PositiveIntegerField(null=True, blank=False, default=None)
    content_object = GenericForeignKey()
    comments = GenericRelation("self")

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
            models.Index(fields=["user"]),
            models.Index(fields=["create_date"]),
        ]
