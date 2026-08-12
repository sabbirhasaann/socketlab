from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from time import sleep
from asyncio import sleep as asysleep


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
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print("....Received ", text_data)
        self.send(
            text_data="Server received you message!"
        )

    def disconnect(self, code):
        print("disconnected...")
