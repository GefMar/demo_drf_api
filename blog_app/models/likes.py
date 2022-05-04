from django.contrib.auth.models import User
from django.db import models

from .posts import Post


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False, related_name="likes")
    create_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name="likes")
