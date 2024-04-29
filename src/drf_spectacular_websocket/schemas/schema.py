from __future__ import annotations

from typing import TYPE_CHECKING, Any

from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf import settings
from django.contrib.admindocs.views import simplify_regex
from django.utils.module_loading import import_string
from drf_spectacular.generators import SchemaGenerator
from typing_extensions import Never  # noqa: UP035

from .consumer_schema import ConsumerAutoSchema, NotReadyError

if TYPE_CHECKING:
    from collections.abc import Callable

    from channels.consumer import AsyncConsumer
    from rest_framework.serializers import Serializer


class WsSchemaGenerator(SchemaGenerator):
    """"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.prepared: dict[str, dict[str, Serializer]] = {'request': {}, 'response': {}}

    def parse(self, input_request: None, public: bool) -> dict[str, Any]:
        result = super().parse(input_request, public)
        ws_result = self.get_ws_endpoints
        result.update(ws_result)
        return result

    @staticmethod
    def get_asgi_application() -> ProtocolTypeRouter:
        return import_string(settings.ASGI_APPLICATION)

    @property
    def get_ws_endpoints(self) -> list[Never] | dict[str, Any]:
        application = self.get_asgi_application()

        socket_routes = application.application_mapping.get('websocket')

        if socket_routes is None:
            return []

        router = socket_routes

        while not isinstance(router, URLRouter):
            router = self._get_router(router)

        result = {}

        for route in router.routes:
            consumer = route.callback.consumer_class()
            result.update(self._find_methods(consumer=consumer, path=simplify_regex(str(route.pattern))))

        return result

    def _get_router(self, middleware: Any) -> Any:
        try:
            return middleware.inner
        except AttributeError:
            try:
                return middleware.application
            except AttributeError:
                return middleware._auths[0]

    def _find_methods(self, consumer: AsyncConsumer, path: str) -> dict[str, Any]:
        consumer_endpoints = {}

        methods_list = self._get_extended_methods_list(consumer)
        while methods_list:
            method = methods_list.pop(0)
            event: str = method.event  # type: ignore[attr-defined]
            name: str = '%s::%s' % (path, event)

            action_schema = self.get_action_schema(method=method)
            try:
                consumer_endpoints[name] = {
                    action_schema.method == 'receive' and 'get' or 'post': {
                        'operationId': f'{event}_{action_schema.get_operation_id()}',
                        'requestBody': action_schema.get_request_body(
                            serializer=action_schema.get_request_serializer(),
                        ),
                        'summary': action_schema.get_summary(),
                        'description': action_schema.get_description(),
                        'tags': action_schema.get_tags(),
                        'responses': action_schema.get_response_bodies(
                            action_schema.get_response_serializers(),
                        ),
                    }
                }
            except NotReadyError:
                methods_list.append(method)

        return consumer_endpoints

    @staticmethod
    def _get_extended_methods_list(consumer: AsyncConsumer) -> list[Callable[..., Any]]:
        methods_list = []
        for attr in dir(consumer):
            method = getattr(consumer, attr)
            if callable(method) and hasattr(method, 'kwargs'):
                methods_list.append(method)
        return methods_list

    def get_action_schema(self, method: Callable[..., Any]) -> ConsumerAutoSchema:
        schema_class = getattr(method, 'kwargs', {}).get('schema', None)
        schema: ConsumerAutoSchema = schema_class()
        schema.method_name = method.__name__
        schema.method = method.type  # type: ignore[attr-defined]
        schema.event = method.event  # type: ignore[attr-defined]
        schema.include_event = method.include_event  # type: ignore[attr-defined]
        schema.registry = self.registry
        schema.prepared = self.prepared
        return schema
