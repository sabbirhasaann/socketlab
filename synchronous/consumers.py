from channels.consumer import SyncConsumer, AsyncConsumer


class MySyncConsumer(SyncConsumer):
    """SyncConsumer"""

    def websokcet_connect(self, event):
        print("WebSocket Connect...")

    def websocket_receive(self, event):
        print("WebSocket Received...")

    def websocket_disconnect(self, event):
        print("WebSocket Disconnect...")


class MyAsyncConsumer(AsyncConsumer):
    """SyncConsumer"""

    async def websokcet_connect(self, event):
        print("WebSocket Connect...")

    async def websocket_receive(self, event):
        print("WebSocket Received...")

    async def websocket_disconnect(self, event):
        print("WebSocket Disconnect...")
