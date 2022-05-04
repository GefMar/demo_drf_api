from rest_framework import serializers

from ...models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("user", "post_id")

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    post_id = serializers.IntegerField(allow_null=False, write_only=True)
