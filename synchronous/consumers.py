from channels.consumer import SyncConsumer


class MySyncConsumer(SyncConsumer):
    """SyncConsumer"""

    def websokcet_connect(self, event):
        print("WebSocket Connect...")

    def websocket_receive(self, event):
        print("WebSocket Received...")

    def websocket_disconnect(self, event):
        print("WebSocket Disconnect...")
