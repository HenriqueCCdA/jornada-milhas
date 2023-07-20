from rest_framework import serializers

from jornada_milhas.core.models import Post


class PostSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "statement",
            "user",
            "photo",
        )
