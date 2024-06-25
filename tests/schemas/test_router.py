from src.drf_spectacular_websocket.schemas.schema import WsSchemaGenerator

from tests.schemas.expected_data import expected_router_schema1


# pytest -s ./tests/schemas/test_router.py::test_router
def test_router() -> None:
    """"""
    generator = WsSchemaGenerator()
    router_schema1 = generator.get_ws_endpoints
    assert router_schema1 == expected_router_schema1
