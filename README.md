# Extend websocket schema decorator for Django Channels

<div align="center">

| Project   |     | Status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------|:----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CI/CD     |     | [![Latest Release](https://github.com/Friskes/drf-spectacular-websocket/actions/workflows/publish-to-pypi.yml/badge.svg)](https://github.com/Friskes/drf-spectacular-websocket/actions/workflows/publish-to-pypi.yml)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Quality   |     | [![Coverage](https://codecov.io/github/Friskes/drf-spectacular-websocket/graph/badge.svg?token=vKez4Pycrc)](https://codecov.io/github/Friskes/drf-spectacular-websocket)                                                                                                                                                                                                                                                                                                                               |
| Package   |     | [![PyPI - Version](https://img.shields.io/pypi/v/drf-spectacular-websocket?labelColor=202235&color=edb641&logo=python&logoColor=edb641)](https://badge.fury.io/py/drf-spectacular-websocket) ![PyPI - Support Python Versions](https://img.shields.io/pypi/pyversions/drf-spectacular-websocket?labelColor=202235&color=edb641&logo=python&logoColor=edb641) ![Project PyPI - Downloads](https://img.shields.io/pypi/dm/drf-spectacular-websocket?logo=python&label=downloads&labelColor=202235&color=edb641&logoColor=edb641)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Meta      |     | [![types - Mypy](https://img.shields.io/badge/types-Mypy-202235.svg?logo=python&labelColor=202235&color=edb641&logoColor=edb641)](https://github.com/python/mypy) [![License - MIT](https://img.shields.io/badge/license-MIT-202235.svg?logo=python&labelColor=202235&color=edb641&logoColor=edb641)](https://spdx.org/licenses/) [![code style - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/format.json&labelColor=202235)](https://github.com/astral-sh/ruff) |

</div>

> Provides [extend_ws_schema](#About-decorator) decorator to documentation [Cunsumer](https://channels.readthedocs.io/en/latest/topics/consumers.html) methods from [channels](https://github.com/django/channels) just like it does [drf-spectacular](https://github.com/tfranzel/drf-spectacular)


## Install
1. Install package
    ```bash
    pip install drf-spectacular-websocket
    ```

2. Create sidecar static
    ```bash
    python manage.py collectstatic
    ```

3. Add app name to `INSTALLED_APPS`
    > `drf_spectacular_websocket` must be higher than `drf_spectacular`
    ```python
    INSTALLED_APPS = [
        'drf_spectacular_websocket',
        'drf_spectacular',
        'drf_spectacular_sidecar',
    ]
    ```


## Configure settings
```python
ASGI_APPLICATION = 'path.to.your.application'

# (Optional) this is default settings are automatically set by the drf_spectacular_websocket.
# You can override them in your application if necessary.
SPECTACULAR_SETTINGS = {
    'DEFAULT_GENERATOR_CLASS': 'drf_spectacular_websocket.schemas.WsSchemaGenerator',
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    'SWAGGER_UI_SETTINGS': {
        'connectSocket': True,  # Automatically establish a WS connection when opening swagger
        'socketMaxMessages': 8,  # Max number of messages displayed in the log window in swagger
        'socketMessagesInitialOpened': False,  # Automatically open the log window when opening swagger
    },
}
```

> drf_spectacular_websocket automatically finds websocket urls and related consumer using `ASGI_APPLICATION` setting.

## About decorator
`extend_ws_schema` decorator accepts one new `type` parameter relative to drf_spectacular `extend_schema`.
- possible values:
    - `send` - Type of interaction, [request -> response]
    - `receive` - Type of interaction, [response without request]

## Usage example

```python
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from rest_framework.serializers import Serializer, CharField
from drf_spectacular_websocket.decorators import extend_ws_schema


class SomeMethodInputSerializer(Serializer):
    some_field = CharField()


class SomeMethodOutputSerializer(Serializer):
    some_field = CharField()


class SendMessageOutputSerializer(Serializer):
    some_field = CharField()


class SomeConsumer(AsyncJsonWebsocketConsumer):

    async def receive_json(self, content, **kwargs):
        some_value = content.get('some_key')
        if some_value:
            await self.some_method(some_value)

    @extend_ws_schema(
        type='send',
        summary='some_method_summary',
        description='some_method_description',
        request=SomeMethodInputSerializer,
        responses=SomeMethodOutputSerializer,
    )
    async def some_method(self, some_value):
        input_serializer = SomeMethodInputSerializer(data=some_value)
        input_serializer.is_valid(raise_exception=True)

        return_value = await some_business_logic(input_serializer.validated_data)

        output_serializer = SomeMethodOutputSerializer(data=return_value)
        output_serializer.is_valid(raise_exception=True)

        await self.send_json(output_serializer.validated_data)

    @extend_ws_schema(
        type='receive',
        summary='send_message_summary',
        description='send_message_description',
        request=None,
        responses=SendMessageOutputSerializer,
    )
    async def send_message(self, message):
        await self.send_json(message)
```

## Contributing
We would love you to contribute to `drf-spectacular-websocket`, pull requests are very welcome! Please see [CONTRIBUTING.md](https://github.com/Friskes/drf-spectacular-websocket/blob/main/CONTRIBUTING.md) for more information.

## Swagger Examples

### Send
![](https://raw.githubusercontent.com/Friskes/drf-spectacular-websocket/main/images/example_send.png)

### Receive
![](https://raw.githubusercontent.com/Friskes/drf-spectacular-websocket/main/images/example_receive.png)
