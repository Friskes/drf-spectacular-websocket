from src.drf_spectacular_websocket.schemas.schema import WsSchemaGenerator

from tests.schemas.expected_schema import expected_schema_1


# python -m pip install .
# pytest -s ./tests
def test_schema() -> None:
    """"""
    generator = WsSchemaGenerator()
    schema_1 = generator.get_schema(request=None, public=True)
    assert schema_1 == expected_schema_1
