from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Room, Message

User = get_user_model()


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "name", "created_at"]


class MessageSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    user_image = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ["id", "content", "username", "user", "user_image", "created_at"]

    def get_user_image(self, obj):
        if obj.user.image:
            return obj.user.image.url
        return None
