from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from typing import Dict, Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views import View
from django.core.cache import cache
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.utils.translation import gettext as _

from .models import Room, RoomMember
from .serializers import RoomSerializer


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get(
        self, request: HttpRequest, *args: str, **kwargs: Dict[str, Any]
    ) -> HttpResponse:
        user_rooms = Room.objects.filter(members__user=request.user).distinct()
        all_rooms = Room.objects.all()

        User = get_user_model()
        online_user_ids = cache.get("online_users", set())
        connected_users = User.objects.filter(id__in=online_user_ids)

        return render(
            request,
            self.template_name,
            {
                "chat_room": user_rooms,
                "all_rooms": all_rooms,
                "users": connected_users,
                "room_range": range(1, 4),
            },
        )


class CreateRoomView(LoginRequiredMixin, View):
    def post(
        self, request: HttpRequest, *args: str, **kwargs: Dict[str, Any]
    ) -> HttpResponse:
        name = request.POST.get("name")
        data = {"name": name}

        serializer = RoomSerializer(data=data)

        if serializer.is_valid():
            try:
                room = serializer.save(creator=request.user)
            except TypeError:
                room = serializer.save()

            RoomMember.objects.create(room=room, user=request.user)

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "rooms",
                {
                    "type": "room_list",
                    "id": serializer.data["id"],
                    "name": serializer.data["name"],
                },
            )

            async_to_sync(channel_layer.group_send)(
                "rooms",
                {
                    "type": "room_joined",
                    "room_id": room.id,
                    "user_id": request.user.id,
                    "room_name": room.name,
                    "is_creator": True,
                },
            )

            return HttpResponseRedirect("/chat/")

        return HttpResponseRedirect("/chat/")


class RoomView(LoginRequiredMixin, View):
    def get(
        self, request: HttpRequest, *args: str, **kwargs: Dict[str, Any]
    ) -> HttpResponse:
        room = Room.objects.get(pk=kwargs["id"])
        user_rooms = Room.objects.filter(members__user=request.user).distinct()
        all_rooms = Room.objects.all()

        return render(
            request,
            "index.html",
            {"room": room, "chat_room": user_rooms, "all_rooms": all_rooms},
        )


class UserView(LoginRequiredMixin, View):
    def get(
        self, request: HttpRequest, *args: str, **kwargs: Dict[str, Any]
    ) -> HttpResponse:
        User = get_user_model()
        online_user_ids = cache.get("online_users", set())
        connected_users = User.objects.filter(id__in=online_user_ids)

        return render(request, "index.html", {"users": connected_users})


class JoinRoomView(LoginRequiredMixin, View):
    def post(
        self, request: HttpRequest, *args: str, **kwargs: Dict[str, Any]
    ) -> HttpResponse:
        room_id = request.POST.get("room_id")

        try:
            room = Room.objects.get(id=room_id)
            room_member, created = RoomMember.objects.get_or_create(
                room=room, user=request.user
            )

            if created:
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    f"chat_{room_id}",
                    {
                        "type": "user_joined",
                        "username": request.user.username,
                        "message": _("%(username)s has joined the chat")
                        % {"username": request.user.username},
                        "user_id": request.user.id,
                    },
                )

                async_to_sync(channel_layer.group_send)(
                    "rooms",
                    {
                        "type": "room_joined",
                        "room_id": int(room_id),
                        "user_id": request.user.id,
                        "room_name": room.name,
                        "is_creator": False,
                    },
                )

            return HttpResponseRedirect("/chat/")

        except Room.DoesNotExist:
            return HttpResponseRedirect("/chat/")


class LeaveRoomView(LoginRequiredMixin, View):
    def post(
        self, request: HttpRequest, *args: str, **kwargs: Dict[str, Any]
    ) -> HttpResponse:
        room_id = request.POST.get("room_id")

        try:
            room = Room.objects.get(id=room_id)
            room_member = RoomMember.objects.get(room=room, user=request.user)
            room_member.delete()

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"chat_{room_id}",
                {
                    "type": "user_left",
                    "username": request.user.username,
                    "message": _("%(username)s has left the chat")
                    % {"username": request.user.username},
                    "user_id": request.user.id,
                },
            )

            async_to_sync(channel_layer.group_send)(
                "rooms",
                {
                    "type": "room_left",
                    "room_id": int(room_id),
                    "user_id": request.user.id,
                },
            )

            return HttpResponseRedirect("/chat/")

        except (Room.DoesNotExist, RoomMember.DoesNotExist):
            return HttpResponseRedirect("/chat/")


class DeleteRoomView(LoginRequiredMixin, View):
    def post(
        self, request: HttpRequest, *args: str, **kwargs: Dict[str, Any]
    ) -> HttpResponse:
        room_id = request.POST.get("room_id")

        try:
            room = Room.objects.get(id=room_id)

            try:
                is_creator = room.creator == request.user
            except AttributeError:
                first_member = (
                    RoomMember.objects.filter(room=room).order_by("joined_at").first()
                )
                is_creator = first_member and first_member.user == request.user

            if is_creator:
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    f"chat_{room_id}",
                    {
                        "type": "room_deleted",
                        "message": _(
                            "Room '%(room_name)s' has been deleted by %(username)s"
                        )
                        % {"room_name": room.name, "username": request.user.username},
                    },
                )

                room.delete()
                return HttpResponseRedirect("/chat/")
            else:
                return HttpResponseRedirect("/chat/")

        except Room.DoesNotExist:
            return HttpResponseRedirect("/chat/")
