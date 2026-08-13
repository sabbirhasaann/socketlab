from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from time import sleep
from asyncio import sleep as asysleep
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
import json
from .models import GenGroup, GenChat


class MyWebsocketConsumer(WebsocketConsumer):

    def connect(self):
        print("Websocket connected..")
        self.accept()
        # self.close()
        self.send(text_data="Message from server")

    def receive(self, text_data=None, bytes_data=None):
        print("Message received from client...", text_data)
        # self.send(text_data="Message from server to client")

        for i in range(10):
            self.send(text_data=str(i))
            sleep(1)

    def disconnect(self, close_code):
        print("Websocket disconnected...", close_code)


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("Websocket connected..")
        await self.accept()
        # self.close()

    async def receive(self, text_data=None, bytes_data=None):
        print("Message received from client...", text_data)
        # await self.send(text_data="Message from server to client")
        for i in range(10):
            await self.send(text_data=str(i))
            await asysleep(1)

    async def disconnect(self, close_code):
        print("Websocket disconnected...", close_code)


class ChatWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print("Channel layer...", self.channel_layer)
        print("Channel name...", self.channel_name)

        self.group_name = self.scope["url_route"]["kwargs"]["channel"]
        async_to_sync(self.channel_layer.group_add)(self.group_name,
                                                    self.channel_name)

        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print("....Received ", text_data)

        data = json.loads(text_data)
        message = data['msg']
        print("Message...", message)

        async_to_sync(self.channel_layer.group_send)(self.group_name, {
            'type': 'chat.message',
            "message": message,
        })

    def chat_message(self, event):
        print("Event...", event)
        self.send(text_data=json.dumps({
            'msg': event['message'],
        }))

    def disconnect(self, code):
        print("disconnected...")


class ChatAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Channel layer...", self.channel_layer)
        print("Channel name...", self.channel_name)

        self.group_name = self.scope["url_route"]["kwargs"]["channel"]
        await self.channel_layer.group_add(self.group_name,
                                           self.channel_name)

        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):

        data = json.loads(text_data)
        self.message = data['msg']
        if self.scope['user'].is_authenticated:
            group = await database_sync_to_async(GenGroup.objects.get)(group=self.group_name)
            chat = GenChat(content=self.message, group=group)
            await database_sync_to_async(chat.save)()

            await self.channel_layer.group_send(self.group_name, {
                'type': 'chat.message',
                "message": self.message,
            })
        else:
            await self.send(
                text_data=json.dumps({
                    'msg': "Login required"
                })
            )

    async def chat_message(self, event):
        print("Event...", event)
        await self.send(text_data=json.dumps({
            'msg': event['message'],
        }))

    async def disconnect(self, code):
        print("disconnected...")
