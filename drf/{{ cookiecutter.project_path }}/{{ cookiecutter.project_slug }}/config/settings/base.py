"""
Django setting's for your project.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

import os
from pathlib import Path

import environ
import structlog

CONFIG_PATH = environ.Path(__file__)

BASE_DIR = Path(CONFIG_PATH - 4)
APPS_DIR = Path(CONFIG_PATH - 3)

env = environ.Env()

env_file = f"{BASE_DIR}/.env"

if os.path.isfile(env_file):
    os.environ.pop("DJANGO_SETTINGS_MODULE")
    environ.Env.read_env(env_file)

CURRENT_ENV = env.str("DJANGO_SETTINGS_MODULE").split(".")[-1]


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEST = False

ALLOWED_HOSTS = ["*"]


# Application definition
PRIORITY_APPS = (
    "whitenoise.runserver_nostatic",
)

DJANGO_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
)

THIRD_PARTY_APPS = (
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "drf_standardized_errors",
    "drf_spectacular",
    "django_structlog",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth.registration",
{% if cookiecutter.google_login %}
    "allauth.socialaccount.providers.google",
{% endif %}
{% if cookiecutter.use_websocket %}
    "channels",
{% endif %}
{% if cookiecutter.use_celery %}
    "django_celery_beat",
{% endif %}
)

LOCAL_APPS = ("accounts",)

EXTRA_APP = ("django_cleanup.apps.CleanupConfig",)

INSTALLED_APPS = PRIORITY_APPS + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + EXTRA_APP

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "django_structlog.middlewares.RequestMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
{% if cookiecutter.camelize_api %}
    "djangorestframework_camel_case.middleware.CamelCaseMiddleWare",
{% endif %}
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

X_FRAME_OPTIONS = "SAMEORIGIN"

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("POSTGRES_DB", ""),
        "USER": env.str("POSTGRES_USER", ""),
        "PASSWORD": env.str("POSTGRES_PASSWORD", ""),
        "HOST": env.str("POSTGRES_HOST", "localhost"),
        "PORT": 5432,
        "OPTIONS": {
            "pool": True,
        },
    }
}

{% if cookiecutter.__use_redis %}
REDIS_HOST = env.str("REDIS_HOST", "")
{% endif %}
# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "{{ cookiecutter.timezone }}"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_ROOT = str(APPS_DIR / "static")
STATIC_URL = "static/"

MEDIA_ROOT = str(BASE_DIR / "media/")
MEDIA_URL = "media/"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "plain_console": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processors": (
                [
                    structlog.stdlib.ProcessorFormatter.remove_processors_meta,
                    structlog.dev.ConsoleRenderer(),
                ]
                if CURRENT_ENV in {"dev", "test"}
                else [
                    structlog.processors.dict_tracebacks,
                    structlog.stdlib.ProcessorFormatter.remove_processors_meta,
                    structlog.processors.JSONRenderer(),
                ]
            ),
        },
        "json_formatter": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processors": [
                structlog.processors.dict_tracebacks,
                structlog.stdlib.ProcessorFormatter.remove_processors_meta,
                structlog.processors.JSONRenderer(),
            ],
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "plain_console",
        }
    },
    "loggers": {
        "uvicorn": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False
        },
        "uvicorn.error": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False
        },
        "uvicorn.access": {},
        "django_structlog": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "django_structlog_{{cookiecutter.project_slug}}": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "{{cookiecutter.project_slug}}": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

# Rest Framework
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
{% if cookiecutter.camelize_api %}
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
{% else  %}
        "rest_framework.renderers.JSONRenderer",
{% endif %}
    ],
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_PARSER_CLASSES": (
{% if cookiecutter.camelize_api %}
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
{% else  %}
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
{% endif %}
    ),
{% if cookiecutter.camelize_api %}
    "JSON_UNDERSCOREIZE": {
        "no_underscore_before_number": True,
    },
{% endif %}
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
    "PAGE_SIZE": 20,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "{{cookiecutter.project_name}} API Documentation",
    "DESCRIPTION": "{{cookiecutter.project_name}} OpenAPI specification",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "CAMELIZE_NAMES": True,
    "COMPONENT_SPLIT_REQUEST": True,
    "COMPONENT_NO_READ_ONLY_REQUIRED": True,
    "SCHEMA_COERCE_PATH_PK_SUFFIX": True,
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
    "SERVE_AUTHENTICATION": ["rest_framework.authentication.BasicAuthentication"],
    "POSTPROCESSING_HOOKS": [
        "drf_spectacular.contrib.djangorestframework_camel_case.camelize_serializer_fields",
        "drf_spectacular.hooks.postprocess_schema_enums",
    ],
    "ENUM_NAME_OVERRIDES": {
        "ValidationErrorEnum": (
            "drf_standardized_errors.openapi_serializers.ValidationErrorEnum.choices"
        ),
        "ClientErrorEnum": (
            "drf_standardized_errors.openapi_serializers.ClientErrorEnum.choices"
        ),
        "ServerErrorEnum": (
            "drf_standardized_errors.openapi_serializers.ServerErrorEnum.choices"
        ),
        "ErrorCode401Enum": (
            "drf_standardized_errors.openapi_serializers.ErrorCode401Enum.choices"
        ),
        "ErrorCode403Enum": (
            "drf_standardized_errors.openapi_serializers.ErrorCode403Enum.choices"
        ),
        "ErrorCode404Enum": (
            "drf_standardized_errors.openapi_serializers.ErrorCode404Enum.choices"
        ),
        "ErrorCode405Enum": (
            "drf_standardized_errors.openapi_serializers.ErrorCode405Enum.choices"
        ),
        "ErrorCode406Enum": (
            "drf_standardized_errors.openapi_serializers.ErrorCode406Enum.choices"
        ),
        "ErrorCode415Enum": (
            "drf_standardized_errors.openapi_serializers.ErrorCode415Enum.choices"
        ),
        "ErrorCode429Enum": (
            "drf_standardized_errors.openapi_serializers.ErrorCode429Enum.choices"
        ),
        "ErrorCode500Enum": (
            "drf_standardized_errors.openapi_serializers.ErrorCode500Enum.choices"
        ),
    },
}

DRF_STANDARDIZED_ERRORS = {
    "ALLOWED_ERROR_STATUS_CODES": [
        "400",
        "401",
        "403",
        "404",
        "405",
        "429",
        "500",
    ],
}

# Custom User
AUTH_USER_MODEL = "accounts.User"
DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL", "webmaster@localhost")

# Social account
SITE_ID = 1

# Dj-rest-auth
REST_AUTH = {
    "USE_JWT": True,
    "SESSION_LOGIN": False,
    "TOKEN_MODEL": None,
    "LOGIN_SERIALIZER": "accounts.serializers.authentication_serializer.LoginSerializer",
    "USER_DETAILS_SERIALIZER": "accounts.serializers.user_serializer.UserSerializer",
    "JWT_AUTH_COOKIE": "{{ cookiecutter.project_path }}-auth",
    "JWT_AUTH_REFRESH_COOKIE": "{{ cookiecutter.project_path }}-refresh",
    "JWT_AUTH_RETURN_EXPIRATION": True,
    "JWT_AUTH_SECURE": True,
    "JWT_AUTH_SAMESITE": "Strict",
}

# CORS
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])
CORS_ALLOW_CREDENTIALS = True

SERVER_URL = env.str("SERVER_URL", 'http://localhost:8000')
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=[SERVER_URL])

# All_auth
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]
ACCOUNT_LOGIN_METHODS = {"email"}

{% if cookiecutter.google_login %}
# Social login

## Google
# https://docs.allauth.org/en/dev/socialaccount/providers/google.html
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "offline",
        },
        "FETCH_USERINFO" : True
    }
}

SOCIAL_LOGIN_CALLBACK_URL_GOOGLE = env.str('SOCIAL_LOGIN_CALLBACK_URL_GOOGLE', '')
{% endif %}

{% if cookiecutter.use_websocket %}
# Django channels configs
ASGI_APPLICATION = "config.asgi.application"
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [REDIS_HOST],
        },
    },
}
{% endif %}

{% if cookiecutter.use_celery %}
# Celery config
CELERY_BROKER_URL = env.str("CELERY_BROKER_URL", REDIS_HOST)
CELERY_RESULT_BACKEND = env.str("CELERY_RESULT_BACKEND", CELERY_BROKER_URL)
CELERY_TASK_DEFAULT_QUEUE = "{{ cookiecutter.project_slug }}_app_worker"

DJANGO_STRUCTLOG_CELERY_ENABLED = True

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
{% endif %}
