from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class MyWebsocketConsumer(WebsocketConsumer):

    def connect(self):
        print("Websocket connected..")
        self.accept()
        # self.close()

    def receive(self, text_data=None, bytes_data=None):
        print("Message received from client...", text_data)
        self.send(text_data="Message from server to client")

    def disconnect(self, close_code):
        print("Websocket disconnected...", close_code)


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("Websocket connected..")
        await self.accept()
        # self.close()

    async def receive(self, text_data=None, bytes_data=None):
        print("Message received from client...", text_data)
        await self.send(text_data="Message from server to client")

    async def disconnect(self, close_code):
        print("Websocket disconnected...", close_code)
