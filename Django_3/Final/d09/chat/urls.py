from django.urls import path
from chat.views import (
    IndexView,
    CreateRoomView,
    RoomView,
    UserView,
    JoinRoomView,
    LeaveRoomView,
    DeleteRoomView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("create-room/", CreateRoomView.as_view(), name="create-room"),
    path("join-room/", JoinRoomView.as_view(), name="join-room"),
    path("leave-room/", LeaveRoomView.as_view(), name="leave-room"),
    path("delete-room/", DeleteRoomView.as_view(), name="delete-room"),
    path("room/<int:id>/", RoomView.as_view(), name="room"),
    path("users/", UserView.as_view(), name="users"),
]
