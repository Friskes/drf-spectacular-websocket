from __future__ import annotations

from typing import TYPE_CHECKING, Any

from drf_spectacular.openapi import AutoSchema
from drf_spectacular.plumbing import (
    build_media_type_object,
    force_instance,
    is_list_serializer,
    is_serializer,
)
from inflection import camelize
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import CharField, Serializer

if TYPE_CHECKING:
    from drf_spectacular.utils import Direction, _SchemaType

    from drf_spectacular_websocket.types import _Type


class EmptySerializer(Serializer):
    pass


class NotReadyError(Exception):
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

    method: _Type
    method_name: str
    event: str
    include_event: bool

    def __init__(self) -> None:
        super().__init__()
        self.prepared: dict[str, dict[str, Serializer]] = {'request': {}, 'response': {}}

    @property
    def view(self) -> EventHandler:
        return EventHandler(name=self.event)

    def get_operation_id(self) -> str:
        return '%s_%s' % (self.method, self.method_name)

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
    ) -> dict[str, Any] | None:
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

    def get_summary(self) -> str:
        return ''

    def _force_ws_serializer(
        self, serializer: Serializer, serializer_type: Direction, direction: _Type | None = None
    ) -> dict[str, Serializer]:
        if serializer is None:
            return {self.event: force_instance(EmptySerializer)}

        serializer = force_instance(serializer)

        if isinstance(serializer, EmptySerializer):
            return {self.event: serializer}

        if direction is None:
            direction = self.method

        if isinstance(serializer, list):
            return self._force_serializers_list(events=serializer, serializer_type=serializer_type)

        if self.event in self.prepared[serializer_type]:
            return {self.event: self.prepared[serializer_type][self.event]}

        if is_list_serializer(serializer):
            serializer_name = serializer.child.__class__.__name__
        elif is_serializer(serializer):
            serializer_name = serializer.__class__.__name__
        else:
            raise AssertionError('Invalid type of serializer')

        name: str = self._get_forced_serializer_name(
            direction=direction, serializer_name=serializer_name
        )

        if is_list_serializer(serializer):
            inner_name: str = 'Ws%sDataSerializer' % self.event.capitalize()
            serializer = type(inner_name, (Serializer,), {self.event: serializer})()

            attrs = {
                'event': CharField(default=self.event),
                'data': serializer,
            }
        else:
            attrs = {
                'event': CharField(default=self.event),
                'data': serializer,
            }

        prepared = type(name, (Serializer,), attrs)() if self.include_event else serializer

        self.prepared[serializer_type][self.event] = prepared
        return {self.event: prepared}

    def _force_serializers_list(self, events: list[str], serializer_type: str) -> dict[str, Serializer]:
        result: dict[str, Serializer] = {}

        for event in events:
            forced = self.prepared[serializer_type].get(event)
            if forced is None:
                raise NotReadyError
            result[event] = forced

        return result

    def _get_forced_serializer_name(self, direction: str, serializer_name: str) -> str:
        name: str = 'Ws%s' % direction.capitalize()
        event: str = camelize(self.event)
        if serializer_name.startswith(event):
            return '%s%s' % (name, serializer_name)

        return '%s%s%s' % (name, event, serializer_name)
