from channels.consumer import SyncConsumer


class MySyncConsumer(SyncConsumer):
    """SyncConsumer"""

    def websocket_connect(self, event):
        print("WebSocket Connect...", event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("WebSocket Received...", event)
        print("Message is ", event['text'])

    def websocket_disconnect(self, event):
        print("WebSocket Disconnect...", event)
