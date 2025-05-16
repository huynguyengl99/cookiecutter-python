from typing import Any

from chanx.generic.websocket import AsyncJsonWebsocketConsumer
from chanx.messages.base import BaseMessage
from chanx.messages.incoming import PingMessage
from chanx.messages.outgoing import PongMessage

from chat.messages import (
    ChatIncomingMessage,
    MessagePayload,
    NewMessage,
    ReplyMessage,
)


class ChatConsumer(AsyncJsonWebsocketConsumer):
    """Websocket to chat"""

    INCOMING_MESSAGE_SCHEMA = ChatIncomingMessage

    async def receive_message(self, message: BaseMessage, **kwargs: Any) -> None:
        match message:
            case PingMessage():
                # Reply with a PONG message
                await self.send_message(PongMessage())
            case NewMessage(payload=new_message_payload):

                # Echo back with a reply message
                await self.send_message(
                    ReplyMessage(
                        payload=MessagePayload(
                            content=f"Reply: {new_message_payload.content}"
                        )
                    )
                )
            case _:
                pass
