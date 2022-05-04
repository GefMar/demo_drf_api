from drf_spectacular.utils import extend_schema
from jsonschema.validators import extend
from notifcations_app.rest_api.versioned.v1.serializers import NotificationSerializer
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ... import models
from ..serializers import LikeSerializer, PostSerializer


class PostViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    serializer_class = PostSerializer
    queryset = models.Post.objects.all()

    @extend_schema(responses={status.HTTP_201_CREATED: PostSerializer(many=True)})
    @action(methods=["POST",], detail=True, serializer_class=None)
    def like(self, request, pk, *args, **kwargs):
        """HELLO DOC STRING"""
        post_instance = self.get_object()
        serialized_like = LikeSerializer(data={"post_id": post_instance.pk}, context={"request": request})
        serialized_like.is_valid(raise_exception=True)
        serialized_like.save()
        return Response(status=status.HTTP_201_CREATED, data=None)
