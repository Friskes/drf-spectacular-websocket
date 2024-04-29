from channels.generic.websocket import JsonWebsocketConsumer
from rest_framework import status
from src.drf_spectacular_websocket.decorators import extend_ws_schema

from tests.serializers import BadOutputSerializer, InputSerializer, OutputSerializer


class Consumer(JsonWebsocketConsumer):
    @extend_ws_schema(
        type='send',
        summary='method_1 summary',
        description='method_1 description',
        request=InputSerializer,
        responses=OutputSerializer,
    )
    def method_1(self) -> None:
        pass

    @extend_ws_schema(
        type='send',
        summary='method_2 summary',
        description='method_2 description',
        request=InputSerializer,
        responses={
            status.HTTP_201_CREATED: OutputSerializer,
            status.HTTP_400_BAD_REQUEST: BadOutputSerializer,
        },
    )
    def method_2(self) -> None:
        pass

    @extend_ws_schema(
        type='receive',
        summary='method_3 summary',
        description='method_3 description',
        request=None,
        responses=OutputSerializer,
    )
    def method_3(self) -> None:
        pass

    @extend_ws_schema(
        type='receive',
        summary='method_4 summary',
        description='method_4 description',
        request=None,
        responses={
            status.HTTP_201_CREATED: OutputSerializer,
            status.HTTP_400_BAD_REQUEST: BadOutputSerializer,
        },
    )
    def method_4(self) -> None:
        pass
