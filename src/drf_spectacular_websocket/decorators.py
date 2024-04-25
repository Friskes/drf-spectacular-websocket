from drf_spectacular.utils import extend_schema

from .schemas.consumer_schema import ConsumerAutoSchema

__all__ = ('extend_ws_schema',)


def extend_ws_schema(
    type: str = 'send',  # noqa: A002
    **kwargs,
):
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

    def decorator(func):
        func.schema = ConsumerAutoSchema
        func.type = type
        func.event = func.__name__
        func.include_event = False
        return extend_schema(type, **kwargs)(func)

    return decorator
