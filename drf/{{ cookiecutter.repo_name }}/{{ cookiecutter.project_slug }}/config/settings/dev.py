from datetime import timedelta

from .base import *  # NOQA

DEBUG = True

INSTALLED_APPS = (
{%- if cookiecutter.use_websocket %}
    ("daphne",) +
{%- endif %}
    INSTALLED_APPS
    + (
        "debug_toolbar",
        "django_extensions",
    )
)


MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] += (
    "rest_framework.renderers.BrowsableAPIRenderer",
)

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INTERNAL_IPS = ["127.0.0.1"]


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
}

SPECTACULAR_SETTINGS = {
    **SPECTACULAR_SETTINGS,
    "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
    "SERVE_AUTHENTICATION": [],
}
