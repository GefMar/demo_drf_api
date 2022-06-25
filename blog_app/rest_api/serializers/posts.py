from rest_framework import serializers

from ...models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ("update_date",)

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    likes_count = serializers.IntegerField(source="likes.count", read_only=True, help_text="FIELD HELP TEXT")
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)
