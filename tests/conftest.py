from django.conf import settings


def pytest_configure() -> None:
    settings.configure(
        ROOT_URLCONF='tests.urls',
        ASGI_APPLICATION='tests.asgi.application',
    )
