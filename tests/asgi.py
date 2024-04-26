from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path

from tests.consumers import Consumer

websocket_urlpatterns = [
    re_path(r'ws/path/$', Consumer.as_asgi()),
]

application = ProtocolTypeRouter(
    {
        'websocket': URLRouter(websocket_urlpatterns),
    }
)
