from __future__ import annotations

from typing import Any

from django.conf import settings

SPECTACULAR_SETTINGS: dict[str, Any] = getattr(settings, 'SPECTACULAR_SETTINGS', {})

SPECTACULAR_SETTINGS['DEFAULT_GENERATOR_CLASS'] = 'drf_spectacular_websocket.schemas.WsSchemaGenerator'
SPECTACULAR_SETTINGS['SWAGGER_UI_DIST'] = 'SIDECAR'
SPECTACULAR_SETTINGS['SWAGGER_UI_FAVICON_HREF'] = 'SIDECAR'
SPECTACULAR_SETTINGS['REDOC_DIST'] = 'SIDECAR'
SWAGGER_UI_SETTINGS: dict[str, Any] = SPECTACULAR_SETTINGS.get('SWAGGER_UI_SETTINGS', {})
SWAGGER_UI_SETTINGS.setdefault('connectSocket', True)
SWAGGER_UI_SETTINGS.setdefault('socketMaxMessages', 8)
SWAGGER_UI_SETTINGS.setdefault('socketMessagesInitialOpened', False)
