from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):
    """my sync consumer"""

    def websocket_connect(self, event):
        print('Websocket is connected...')
        self.send({
            "type": 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("Message received", event['text'])
        self.send({
            'type': 'websocket.send',
            'text': 'Message sent from sync 1 server'
        })

    def websocket_disconnect(self, event):
        print('Websocket disconnected...')
        raise StopConsumer()
