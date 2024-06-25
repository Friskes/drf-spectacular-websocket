from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels_auth_token_middlewares.middleware.drf import (
    SimpleJWTAuthTokenMiddlewareStack,
)
from django.urls import path

from tests.consumers import Consumer

websocket_urlpatterns = [
    path('consumer-path/', Consumer.as_asgi()),
]

application = ProtocolTypeRouter(
    {
        'websocket': AllowedHostsOriginValidator(
            URLRouter(
                [
                    path(
                        'A/',
                        SimpleJWTAuthTokenMiddlewareStack(
                            URLRouter(
                                [
                                    path(
                                        'AA/',
                                        URLRouter(websocket_urlpatterns),
                                    ),
                                    path(
                                        'AB/',
                                        URLRouter(
                                            [
                                                path('AAA/', URLRouter(websocket_urlpatterns)),
                                            ]
                                        ),
                                    ),
                                ]
                            ),
                        ),
                    ),
                    path(
                        'B/',
                        AuthMiddlewareStack(
                            URLRouter(websocket_urlpatterns),
                        ),
                    ),
                ]
            )
        )
    }
)
