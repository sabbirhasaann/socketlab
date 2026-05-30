from channels.consumer import AsyncConsumer


class MyAsyncConsumer(AsyncConsumer):
    """SyncConsumer"""

    async def websocket_connect(self, event):
        print("WebSocket Connect...", event)

    async def websocket_receive(self, event):
        print("WebSocket Received...", event)

    async def websocket_disconnect(self, event):
        print("WebSocket Disconnect...", event)
