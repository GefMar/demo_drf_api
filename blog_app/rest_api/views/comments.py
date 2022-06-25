from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from ... import models
from ..serializers import CommentSerializer

__all__ = ("CommentViewSet",)


class CommentViewSet(GenericViewSet, RetrieveModelMixin):
    serializer_class = CommentSerializer
    queryset = models.Comment.objects.all()
