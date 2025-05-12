from channels.routing import URLRouter

from chanx.urls import path

ws_all_routes = URLRouter([])

ws_routes = URLRouter(
    [
        path("ws/", ws_all_routes),
    ]
)
