from rest_framework import routers

from .views import NotificationsViewSet

api_router = routers.DefaultRouter()

api_router.register("notification", NotificationsViewSet)
