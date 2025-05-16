from channels.routing import URLRouter

from chanx.routing import path

ws_router = URLRouter([])

router = URLRouter(
    [
        path("ws/", ws_router),
    ]
)
