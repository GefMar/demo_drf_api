from rest_framework import routers

from .views import PostViewSet

api_router = routers.DefaultRouter()

api_router.register("post", PostViewSet, basename="post")
