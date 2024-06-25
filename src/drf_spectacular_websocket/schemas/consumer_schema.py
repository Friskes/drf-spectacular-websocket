from __future__ import annotations

from typing import TYPE_CHECKING, Any

from drf_spectacular.openapi import AutoSchema
from drf_spectacular.plumbing import (
    build_media_type_object,
    force_instance,
    is_list_serializer,
)
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import Serializer

if TYPE_CHECKING:
    from drf_spectacular.utils import Direction, _SchemaType

    from drf_spectacular_websocket.types import WsMethod


class EmptySerializer(Serializer):
    pass


class EventHandler:
    request = None
    kwargs: dict[str, Any] = {}
    versioning_class = None

    def __init__(self, name: str) -> None:
        self.name = name

    def get_parsers(self) -> list[JSONParser]:
        return [JSONParser]

    def get_renderers(self) -> list[JSONRenderer]:
        return [JSONRenderer]

    def determine_version(self, *args: Any, **kwargs: Any) -> tuple[None, None]:
        return None, None


class ConsumerAutoSchema(AutoSchema):
    """"""

    method: WsMethod
    method_name: str
    event: str

    def __init__(self) -> None:
        super().__init__()
        self.prepared: dict[Direction, dict[str, Serializer]] = {'request': {}, 'response': {}}

    @property
    def view(self) -> EventHandler:
        return EventHandler(name=self.event)

    def get_operation_id(self) -> str:
        return f'{self.method}_{self.method_name}'

    def get_request_body(self, serializer: Serializer) -> dict[str, dict[str, _SchemaType]] | None:
        """"""
        _, serializer = self._force_ws_serializer(
            serializer=serializer, serializer_type='request'
        ).popitem()

        schema, _ = self._get_request_for_media_type(serializer)
        if schema is None:
            return None

        content = [
            (media_type, schema, self._get_examples(serializer, 'request', media_type))
            for media_type in self.map_parsers()
        ]

        return {
            'content': {
                media_type: build_media_type_object(schema, examples)
                for media_type, schema, examples in content
            }
        }

    def _get_request_for_media_type(
        self, serializer: Serializer, direction: Direction = 'request'
    ) -> tuple[_SchemaType | None, bool]:
        """"""
        component = self.resolve_serializer(serializer, direction)

        if not component:
            # serializer is empty so skip content enumeration
            return None, False

        schema = component.ref
        return schema, True

    def get_response_bodies(
        self, response_serializers: Serializer | dict[int, Serializer]
    ) -> _SchemaType | None:
        """"""
        if not response_serializers:
            return None

        if isinstance(response_serializers, dict):
            return {
                f'{self.event}   {code}': self._get_response_for_code(force_instance(serializer), code)
                for code, serializer in response_serializers.items()
            }

        serializers_ = self._force_ws_serializer(
            serializer=response_serializers, serializer_type='response', direction='receive'
        )

        return {
            f'{event}   {status.HTTP_200_OK}': self._get_response_for_code(
                serializer, status.HTTP_200_OK
            )
            for event, serializer in serializers_.items()
        }

    def _get_serializer_name(
        self, serializer: Serializer, direction: str, bypass_extensions: bool = False
    ) -> str:
        return type(serializer).__name__

    def get_tags(self) -> list[str]:
        return ['web_socket']

    def _force_ws_serializer(
        self, serializer: Serializer, serializer_type: Direction, direction: WsMethod | None = None
    ) -> dict[str, Serializer]:
        """"""
        if serializer is None:
            return {self.event: force_instance(EmptySerializer)}

        serializer = force_instance(serializer)

        if direction is None:
            direction = self.method

        if self.event in self.prepared[serializer_type]:
            return {self.event: self.prepared[serializer_type][self.event]}

        if is_list_serializer(serializer):
            inner_name: str = f'Ws{self.event.capitalize()}DataSerializer'

            serializer = type(inner_name, (Serializer,), {self.event: serializer})()

        self.prepared[serializer_type][self.event] = serializer
        return {self.event: serializer}
