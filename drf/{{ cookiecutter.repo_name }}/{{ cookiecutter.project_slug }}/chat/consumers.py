import asyncio

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    """Websocket to chat"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.group_name = None

    async def websocket_connect(self, message):
        await super().websocket_connect(message)
        if self.scope.get("user"):
            self.user = self.scope["user"]
            await self.channel_layer.group_add(self.group_name, self.channel_name)

    async def disconnect(self, close_code=None):
        await super().disconnect(close_code)
        if self.group_name:
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content: dict, **kwargs):
        message = content.get("message", "")
        await self.send_json({"message": f"Reply: {message}"})
        await asyncio.sleep(0)

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        if text_data:
            await self.receive_json(await self.decode_json(text_data), **kwargs)
        elif bytes_data:
            byte_len = len(bytes_data)
            await self.send_json({"message": f"Byte length: {byte_len}"})
        else:
            raise ValueError("No text section for incoming WebSocket frame!")
