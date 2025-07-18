from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from django.utils.translation import gettext as _
from .models import Room, Message, RoomMember
from .serializers import MessageSerializer


class RoomListConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("rooms", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("rooms", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data.get("type")

        if message_type == "leave_room":
            await self.handle_leave_room(data)
        elif message_type == "room_deleted":
            await self.handle_delete_room(data)

    async def handle_leave_room(self, data):
        room_id = data.get("room_id")
        user = self.scope["user"]

        if user.is_authenticated:
            try:
                await self.remove_user_from_room(room_id, user)

                await self.channel_layer.group_send(
                    f"chat_{room_id}",
                    {
                        "type": "user_left",
                        "username": user.username,
                        "message": _("%(username)s has left the chat")
                        % {"username": user.username},
                        "user_id": user.id,
                    },
                )

                await self.channel_layer.group_send(
                    "rooms",
                    {
                        "type": "room_left",
                        "room_id": room_id,
                        "user_id": user.id,
                        "success": True,
                    },
                )
            except Exception as e:
                print(f"Error leaving room: {e}")

    async def handle_delete_room(self, data):
        room_id = data.get("room_id")
        user = self.scope["user"]

        if user.is_authenticated:
            try:
                can_delete = await self.can_delete_room(room_id, user)

                if can_delete:
                    room_name = await self.get_room_name(room_id)

                    await self.channel_layer.group_send(
                        f"chat_{room_id}",
                        {
                            "type": "room_deleted",
                            "message": _(
                                "Room '%(room_name)s' has been deleted by %(username)s"
                            )
                            % {"room_name": room_name, "username": user.username},
                        },
                    )

                    await self.delete_room(room_id)

                    await self.send(
                        text_data=json.dumps(
                            {
                                "type": "room_deleted",
                                "room_id": room_id,
                                "success": True,
                                "message": _(
                                    "Room '%(room_name)s' has been deleted by %(username)s"
                                )
                                % {"room_name": room_name, "username": user.username},
                            }
                        )
                    )
                else:
                    await self.send(
                        text_data=json.dumps(
                            {
                                "type": "room_deleted",
                                "room_id": room_id,
                                "success": False,
                                "message": _(
                                    "You are not authorized to delete this room"
                                ),
                            }
                        )
                    )
            except Exception as e:
                print(f"Error deleting room: {e}")

    async def room_joined(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "type": "room_joined",
                    "room_id": event["room_id"],
                    "user_id": event["user_id"],
                    "room_name": event["room_name"],
                    "is_creator": event["is_creator"],
                }
            )
        )

    async def room_list(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "type": "room_created",
                    "id": event["id"],
                    "name": event["name"],
                }
            )
        )

    async def room_left(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "type": "room_left",
                    "room_id": event["room_id"],
                    "user_id": event["user_id"],
                    "success": event.get("success", True),
                }
            )
        )

    @database_sync_to_async
    def can_delete_room(self, room_id, user):
        try:
            room = Room.objects.get(id=room_id)
            try:
                return room.creator == user
            except AttributeError:
                first_member = (
                    RoomMember.objects.filter(room=room).order_by("joined_at").first()
                )
                return first_member and first_member.user == user
        except Room.DoesNotExist:
            return False

    @database_sync_to_async
    def get_room_name(self, room_id):
        try:
            return Room.objects.get(id=room_id).name
        except Room.DoesNotExist:
            return "Unknown Room"

    @database_sync_to_async
    def delete_room(self, room_id):
        try:
            Room.objects.get(id=room_id).delete()
        except Room.DoesNotExist:
            pass

    @database_sync_to_async
    def remove_user_from_room(self, room_id, user):
        try:
            room = Room.objects.get(id=room_id)
            RoomMember.objects.get(room=room, user=user).delete()
        except (Room.DoesNotExist, RoomMember.DoesNotExist):
            pass


class OnlineUsersConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "online_users"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        if self.scope["user"].is_authenticated:
            await self.add_user_to_online_list()
            await self.broadcast_user_list()

    async def disconnect(self, close_code):
        if self.scope["user"].is_authenticated:
            await self.remove_user_from_online_list()
            await self.broadcast_user_list()

        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def broadcast_user_list(self):
        online_users = await self.get_online_users()
        await self.channel_layer.group_send(
            self.group_name, {"type": "user_list_update", "users": online_users}
        )

    async def user_list_update(self, event):
        await self.send(
            text_data=json.dumps({"type": "user_list", "users": event["users"]})
        )

    @database_sync_to_async
    def add_user_to_online_list(self):
        from django.core.cache import cache

        online_users = cache.get("online_users", set())
        online_users.add(self.scope["user"].id)
        cache.set("online_users", online_users, timeout=None)

    @database_sync_to_async
    def remove_user_from_online_list(self):
        from django.core.cache import cache

        online_users = cache.get("online_users", set())
        online_users.discard(self.scope["user"].id)
        cache.set("online_users", online_users, timeout=None)

    @database_sync_to_async
    def get_online_users(self):
        from django.core.cache import cache

        User = get_user_model()
        online_user_ids = cache.get("online_users", set())
        users = User.objects.filter(id__in=online_user_ids)
        return [
            {
                "id": user.id,
                "username": user.username,
                "image": user.image.url if user.image else None,
            }
            for user in users
        ]


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = f"chat_{self.room_id}"

        if self.scope["user"].is_authenticated:
            is_member = await self.check_room_membership()
            if not is_member:
                await self.close()
                return

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        messages = await self.get_room_messages()
        await self.send(
            text_data=json.dumps({"type": "message_history", "messages": messages})
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_content = data["message"]

        if self.scope["user"].is_authenticated and message_content.strip():
            message = await self.save_message(message_content)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                },
            )

    async def chat_message(self, event):
        await self.send(
            text_data=json.dumps({"type": "message", "message": event["message"]})
        )

    async def user_joined(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "type": "notification",
                    "message": event["message"],
                    "username": event["username"],
                }
            )
        )

    async def user_left(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "type": "notification",
                    "message": event["message"],
                    "username": event["username"],
                }
            )
        )

    async def room_deleted(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "type": "room_deleted",
                    "message": event["message"],
                }
            )
        )

    @database_sync_to_async
    def save_message(self, content):
        room = Room.objects.get(id=self.room_id)
        message = Message.objects.create(
            room=room, user=self.scope["user"], content=content
        )
        return MessageSerializer(message).data

    @database_sync_to_async
    def check_room_membership(self):
        try:
            room = Room.objects.get(id=self.room_id)
            return RoomMember.objects.filter(
                room=room, user=self.scope["user"]
            ).exists()
        except Room.DoesNotExist:
            return False

    @database_sync_to_async
    def get_room_messages(self):
        try:
            room = Room.objects.get(id=self.room_id)
            messages = Message.objects.filter(room=room).order_by("created_at")
            return MessageSerializer(messages, many=True).data
        except Room.DoesNotExist:
            return []
