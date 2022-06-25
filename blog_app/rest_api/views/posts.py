from django.db import IntegrityError
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ... import models
from ..serializers import CommentSerializer, PostSerializer


class PostViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    serializer_class = PostSerializer
    queryset = models.Post.objects.all()

    action_serializer_classes = {
        "like": None,
        "comment": CommentSerializer,
        "comments": CommentSerializer,
    }

    def get_serializer_class(self):
        return self.action_serializer_classes.get(self.action, self.serializer_class)

    @extend_schema(responses={status.HTTP_201_CREATED: None, status.HTTP_409_CONFLICT: None})
    @action(methods=["POST",], detail=True, pagination_class=None)
    def like(self, request, pk, *args, **kwargs):
        """HELLO DOC STRING"""

        post_instance = self.get_object()
        try:
            models.Like.objects.create(content_object=post_instance, user=request.user)
        except IntegrityError:
            return Response(status=status.HTTP_409_CONFLICT, data=None)
        return Response(status=status.HTTP_201_CREATED, data=None)

    @action(methods=["POST"], detail=True, pagination_class=None)
    def comment(self, request, pk, *args, **kwargs):
        """DOC STRING COMMENTS For Action"""

        result = super(PostViewSet, self).create(request, pk, *args, **kwargs)
        return result

    @extend_schema(responses={status.HTTP_200_OK: CommentSerializer(many=True)})
    @action(methods=["GET"], detail=True)
    def comments(self, request, pk):
        post_instance = self.get_object()
        queryset = post_instance.comments.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
