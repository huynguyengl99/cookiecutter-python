from channels.routing import URLRouter

from chanx.routing import include, path

ws_router = URLRouter(
    [
        path("chat/", include("chat.routing")),
    ]
)

router = URLRouter(
    [
        path("ws/", ws_router),
    ]
)
