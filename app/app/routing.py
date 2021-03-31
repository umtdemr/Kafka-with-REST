from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from logs.consumers import LogConsumer


application = ProtocolTypeRouter(
    {
        "websocket": URLRouter(
            [
                path("logs", LogConsumer.as_asgi()),
            ]
        )
    }
)
