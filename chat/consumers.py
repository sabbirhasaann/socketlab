from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from .models import Chat, Group
import json


class MySyncConsumer(SyncConsumer):
    """my sync consumer"""

    def websocket_connect(self, event):
        print('Websocket is connected...')
        print("Channel Layer", self.channel_layer)
        print("Channel name", self.channel_name)

        self.group_name = self.scope['url_route']['kwargs']['group_name']
        print("Group name ...", self.group_name)

        # add a channe to a new or existing groups
        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name,
        )

        self.send({
            "type": 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("Message received", event['text'])
        print("Type of received Message", type(event['text']))

        data = json.loads(event['text'])

        print("User from reqs.....", self.scope['user'])

        if self.scope['user'].is_authenticated:
            self.username = self.scope['user'].get_username()

            print("User name....", self.username)

            group = Group.objects.get(name=self.group_name)
            chat = Chat.objects.create(content=data['msg'], group=group)
            chat.save()

            data['username'] = self.username

            async_to_sync(self.channel_layer.group_send)(self.group_name, {
                'type': 'chat.message',
                'message': json.dumps(data)
            })
        else:
            self.send({
                'type': 'websocket.send',
                'text': json.dumps({"msg": "Login required", "username": "Guest"})
            })

    def chat_message(self, event):
        print("Event...", event)
        print("Actual data", event['message'])
        print("Type of actual data", type(event['message']))
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    def websocket_disconnect(self, event):
        print('Websocket disconnected...')
        print("Channel Layer", self.channel_layer)
        print("Channel name", self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            'Programmers', self.channel_name,
        )
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    """My async consumer"""

    async def websocket_connect(self, event):
        print("Websocket connecting...")
        print("Default channel layer: ", self.channel_layer)
        print("Channel name: ", self.channel_name)
        # print("Print self.scope....", self.scope)
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        print("group name..", self.scope['url_route']['kwargs']['group_name'])
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.send({
            'type': 'websocket.accept',
        })
        print('Websocket connected!')

    async def websocket_receive(self, event):
        print("Received message", event['text'])

        await self.channel_layer.group_send(self.group_name, {
            'type': 'chat.message',
            'message': event['text']
        })

    async def chat_message(self, event):
        print("Chat message: ", event['message'])
        await self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    async def websocket_disconnect(self, event):
        print('Websocket disconnecting...')
        print("Websocket channel layer: ", self.channel_layer)
        print("Websocket channel name: ", self.channel_name)
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        raise StopConsumer()
