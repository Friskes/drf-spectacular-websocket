from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable  # noqa: UP035

from drf_spectacular.utils import extend_schema

from .schemas.consumer_schema import ConsumerAutoSchema

if TYPE_CHECKING:
    from src.drf_spectacular_websocket.types import DecoratedCallable

    from drf_spectacular_websocket.types import WsMethod

__all__ = ('extend_ws_schema',)


def extend_ws_schema(
    type: WsMethod = 'send',  # noqa: A002
    **kwargs: Any,
) -> Callable[[DecoratedCallable], DecoratedCallable]:
    """
    - `type`
        - `send` - Type of interaction, [request -> response]
        - `receive` - Type of interaction, [response without request]
    ---
    - Example request:
        - request=None
        - request=SomeSerializer

    - Example responses:
        - responses=SomeSerializer
        - responses=SomeSerializer(many=True)
        - responses={200: Some1Serializer, 201: Some2Serializer}
    """

    def decorator(func: DecoratedCallable) -> DecoratedCallable:
        func.schema = ConsumerAutoSchema  # type: ignore[attr-defined]
        func.type = type  # type: ignore[attr-defined]
        func.event = func.__name__  # type: ignore[attr-defined]
        return extend_schema(type, **kwargs)(func)

    return decorator
