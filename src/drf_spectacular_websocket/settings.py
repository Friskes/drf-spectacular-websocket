from django.conf import settings

SPECTACULAR_SETTINGS: dict = getattr(settings, 'SPECTACULAR_SETTINGS', {})

SPECTACULAR_SETTINGS['DEFAULT_GENERATOR_CLASS'] = 'drf_spectacular_websocket.schemas.WsSchemaGenerator'
SPECTACULAR_SETTINGS['SWAGGER_UI_DIST'] = 'SIDECAR'
SPECTACULAR_SETTINGS['SWAGGER_UI_FAVICON_HREF'] = 'SIDECAR'
SPECTACULAR_SETTINGS['REDOC_DIST'] = 'SIDECAR'
SWAGGER_UI_SETTINGS: dict = SPECTACULAR_SETTINGS.get('SWAGGER_UI_SETTINGS', {})
SWAGGER_UI_SETTINGS.setdefault('connectSocket', True)
SWAGGER_UI_SETTINGS.setdefault('socketMaxMessages', 8)
SWAGGER_UI_SETTINGS.setdefault('socketMessagesInitialOpened', False)
