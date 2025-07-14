from django.urls import re_path
from .consumers import RoomListConsumer, OnlineUsersConsumer, ChatConsumer

websocket_urlpatterns = [
    re_path(r"ws/rooms/$", RoomListConsumer.as_asgi()),
    re_path(r"ws/users/$", OnlineUsersConsumer.as_asgi()),
    re_path(r"ws/chat/(?P<room_id>\d+)/$", ChatConsumer.as_asgi()),
]
