from rest_framework import serializers

from jornada_milhas.core.models import Destination, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "statement",
            "user",
            "photo",
        )


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = (
            "id",
            "name",
            "price",
            "photo",
        )
