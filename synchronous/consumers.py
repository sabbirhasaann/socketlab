from channels.consumer import SyncConsumer, AsyncConsumer


class MySyncConsumer(SyncConsumer):
    """SyncConsumer"""

    def websocket_connect(self, event):
        print("WebSocket Connect...", event)

    def websocket_receive(self, event):
        print("WebSocket Received...", event)

    def websocket_disconnect(self, event):
        print("WebSocket Disconnect...", event)


class MyAsyncConsumer(AsyncConsumer):
    """SyncConsumer"""

    async def websocket_connect(self, event):
        print("WebSocket Connect...", event)

    async def websocket_receive(self, event):
        print("WebSocket Received...", event)

    async def websocket_disconnect(self, event):
        print("WebSocket Disconnect...", event)
