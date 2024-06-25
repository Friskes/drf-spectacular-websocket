import django
from django.conf import settings


def pytest_configure() -> None:
    settings.configure(
        ROOT_URLCONF='tests.urls',
        ASGI_APPLICATION='tests.asgi.application',
        SECRET_KEY='super-puper-secret-key',
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
        ),
    )
    django.setup()
