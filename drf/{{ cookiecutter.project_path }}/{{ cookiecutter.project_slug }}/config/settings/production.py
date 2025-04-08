from .base import *  # NOQA

from urllib.parse import urlparse

SECRET_KEY = env.str("DJANGO_SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": "psqlextra.backend",
        "NAME": env.str("POSTGRES_DB"),
        "USER": env.str("POSTGRES_USER"),
        "PASSWORD": env.str("POSTGRES_PASSWORD"),
        "HOST": env.str("POSTGRES_HOST"),
        "PORT": 5432,
    }
}

HOST_URLS = env.list("HOST_URLS", default=[])

if HOST_URLS:
    CSRF_TRUSTED_ORIGINS = HOST_URLS
    ALLOWED_HOSTS = [urlparse(url).netloc for url in HOST_URLS]
    SECURE_SSL_REDIRECT = True
else:
    CSRF_TRUSTED_ORIGINS = []
    ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS += env.list("CSRF_TRUSTED_ORIGINS", default=[])

CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Media storage
# Uncomment the below codes to use Google Cloud Storage
# Remember to set GS_BUCKET_NAME
# See more at https://django-storages.readthedocs.io/en/latest/
# STORAGES["default"] = {
#     "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
#     "OPTIONS": {
#         "bucket_name": env.str("GS_BUCKET_NAME"),
#         "querystring_auth": False,
#     }
# }
