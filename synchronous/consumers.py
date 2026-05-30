from channels.consumer import SyncConsumer


class MySyncConsumer(SyncConsumer):
    """SyncConsumer"""

    def websocket_connect(self, event):
        print("WebSocket Connect...", event)

    def websocket_receive(self, event):
        print("WebSocket Received...", event)

    def websocket_disconnect(self, event):
        print("WebSocket Disconnect...", event)
