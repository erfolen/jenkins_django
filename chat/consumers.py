import json
import aioredis

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Соединение с Redis
        self.redis = aioredis.from_url('redis://localhost:6379', encoding="utf-8", decode_responses=True)

        # Присоединение группы к чату
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

        # Увеличиваем счетчик активных пользователей
        await self.redis.incr(f'{self.room_group_name}_active_users')

        # Получение старых сообщений из Redis
        messages = await self.redis.lrange(f'chat_messages_{self.room_group_name}', 0, -1)
        messages = [json.loads(msg) for msg in messages]

        await self.send(text_data=json.dumps({
            'type': 'old_messages',
            'messages': messages
        }))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

       # Уменьшаем счетчик активных пользователей
        active_users = await self.redis.decr(f'{self.room_group_name}_active_users')
        if active_users == 0:  # Добавлено
            await self.redis.expire(f'chat_messages_{self.room_group_name}', 300)
        await self.redis.close()

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = text_data_json['user']

        #Сохранение сообщение в Redis
        new_message = {
            'user': user,
            'message': message
        }
        await self.redis.rpush(f'chat_messages_{self.room_group_name}', json.dumps(new_message))
        await self.redis.expire(f'chat_messages_{self.room_group_name}', 300)  # Обновление ТТL при получении сообщения

        # Отправка сообщения в группу чата
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message, "user": user}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        user = event["user"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"type": "chat", "message": message, "user": user}))
