from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from .comments import Comment
from .likes import Like


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=120, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    likes = GenericRelation(Like)
    comments = GenericRelation(Comment)

    class Meta:
        indexes = [models.Index(fields=["user"]), models.Index(fields=["create_date"])]
