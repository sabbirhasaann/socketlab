from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
from asyncio import sleep


class MyAsyncConsumer(AsyncConsumer):
    """SyncConsumer"""

    async def websocket_connect(self, event):
        print("WebSocket Connect...", event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("WebSocket Received...", event)
        print("Message is ", event['text'])
        for i in range(50):
            await self.send({
                'type': 'websocket.send',
                'text': str(i)
            })
            await sleep(1)

    async def websocket_disconnect(self, event):
        print("WebSocket Disconnect...", event)
        raise StopConsumer()
