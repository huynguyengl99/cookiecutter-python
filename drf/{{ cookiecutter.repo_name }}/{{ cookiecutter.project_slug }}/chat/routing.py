from channels.routing import URLRouter

from chanx.routing import path

from chat.consumers import ChatConsumer

router = URLRouter([
    path("", ChatConsumer.as_asgi()),
])
