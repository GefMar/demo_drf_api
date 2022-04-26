from notifcations_app import models
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers import NotificationSerializer


class NotificationsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    serializer_class = NotificationSerializer
    queryset = models.Notification.objects.all()
