from rest_framework import serializers

from ...models import Comment


class CurrentPostDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context["view"].get_object()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = (
            "object_id",
            "content_type",
        )

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    likes_count = serializers.IntegerField(source="likes.count", read_only=True, help_text="HELP TEXT Like COUNT")
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)
    content_object = serializers.HiddenField(default=CurrentPostDefault())
    comments = serializers.ListSerializer(allow_empty=True, child=serializers.IntegerField(), read_only=True)
