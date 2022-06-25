from rest_framework import routers

from .views import CommentViewSet, PostViewSet

api_router = routers.DefaultRouter()

api_router.register("post", PostViewSet, basename="post")
api_router.register("comment", CommentViewSet, basename="comment")
