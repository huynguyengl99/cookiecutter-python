from .base import *  # NOQA

SECRET_KEY = env.str("DJANGO_SECRET_KEY")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

INSTALLED_APPS += ["anymail"]
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
{%- if cookiecutter.mail_service == 'Mailgun' %}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
ANYMAIL = {
    "MAILGUN_API_KEY": env("MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": env("MAILGUN_DOMAIN"),
    "MAILGUN_API_URL": env("MAILGUN_API_URL", default="https://api.mailgun.net/v3"),
}
{%- elif cookiecutter.mail_service == 'Amazon SES' %}
EMAIL_BACKEND = "anymail.backends.amazon_ses.EmailBackend"
ANYMAIL = {}
{%- elif cookiecutter.mail_service == 'Mailjet' %}
EMAIL_BACKEND = "anymail.backends.mailjet.EmailBackend"
ANYMAIL = {
    "MAILJET_API_KEY": env("MAILJET_API_KEY"),
    "MAILJET_SECRET_KEY": env("MAILJET_SECRET_KEY"),
}
{%- elif cookiecutter.mail_service == 'Mandrill' %}
EMAIL_BACKEND = "anymail.backends.mandrill.EmailBackend"
ANYMAIL = {
    "MANDRILL_API_KEY": env("MANDRILL_API_KEY"),
    "MANDRILL_API_URL": env("MANDRILL_API_URL", default="https://mandrillapp.com/api/1.0"),
}
{%- elif cookiecutter.mail_service == 'Postmark' %}
EMAIL_BACKEND = "anymail.backends.postmark.EmailBackend"
ANYMAIL = {
    "POSTMARK_SERVER_TOKEN": env("POSTMARK_SERVER_TOKEN"),
    "POSTMARK_API_URL": env("POSTMARK_API_URL", default="https://api.postmarkapp.com/"),
}
{%- elif cookiecutter.mail_service == 'Sendgrid' %}
EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
ANYMAIL = {
    "SENDGRID_API_KEY": env("SENDGRID_API_KEY"),
    "SENDGRID_API_URL": env("SENDGRID_API_URL", default="https://api.sendgrid.com/v3/"),
}
{%- elif cookiecutter.mail_service == 'Brevo' %}
EMAIL_BACKEND = "anymail.backends.brevo.EmailBackend"
ANYMAIL = {
    "BREVO_API_KEY": env("BREVO_API_KEY"),
    "BREVO_API_URL": env("BREVO_API_URL", default="https://api.brevo.com/v3/"),
}
{%- elif cookiecutter.mail_service == 'SparkPost' %}
EMAIL_BACKEND = "anymail.backends.sparkpost.EmailBackend"
ANYMAIL = {
    "SPARKPOST_API_KEY": env("SPARKPOST_API_KEY"),
    "SPARKPOST_API_URL": env("SPARKPOST_API_URL", default="https://api.sparkpost.com/api/v1"),
}
{%- elif cookiecutter.mail_service == 'MailerSend' %}
EMAIL_BACKEND = "anymail.backends.mailersend.EmailBackend"
ANYMAIL = {
    "MAILERSEND_API_TOKEN": ": env("MAILERSEND_API_TOKEN"),
}
{%- elif cookiecutter.mail_service == 'Postal' %}
EMAIL_BACKEND = "anymail.backends.postal.EmailBackend"
ANYMAIL = {
    "POSTAL_API_KEY": env("POSTAL_API_KEY"),
    "POSTAL_API_URL": env("POSTAL_API_URL"),
}
{%- elif cookiecutter.mail_service == 'Resend' %}
EMAIL_BACKEND = "anymail.backends.resend.EmailBackend"
ANYMAIL = {
    "RESEND_API_KEY": env("RESEND_API_KEY"),
    "RESEND_API_URL": env("RESEND_API_URL", default="https://api.resend.com/"),
}
{%- elif cookiecutter.mail_service == 'Unisender Go' %}
EMAIL_BACKEND = "anymail.backends.unisender_go.EmailBackend"
ANYMAIL = {
    "UNISENDER_GO_API_KEY": env("UNISENDER_GO_API_KEY"),
    "UNISENDER_GO_API_URL": env("UNISENDER_GO_API_URL", default="https://go2.unisender.ru/ru/transactional/api/v1/"),
}
{%- elif cookiecutter.mail_service == 'Other SMTP' %}
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
ANYMAIL = {}
{%- endif %}

{%- if cookiecutter.cloud_provider == 'AWS' %}
AWS_ACCESS_KEY_ID = env("DJANGO_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("DJANGO_AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("DJANGO_AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env("DJANGO_AWS_S3_REGION_NAME", default=None)

STORAGES["default"] = {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"}
{% elif cookiecutter.cloud_provider == 'GCP' %}
GS_BUCKET_NAME = env("DJANGO_GCP_STORAGE_BUCKET_NAME")
GOOGLE_APPLICATION_CREDENTIALS = env.str("GOOGLE_APPLICATION_CREDENTIALS", "")

STORAGES["default"] = {"BACKEND": "storages.backends.gcloud.GoogleCloudStorage"}
{% elif cookiecutter.cloud_provider == 'Azure' %}
AZURE_ACCOUNT_KEY = env("DJANGO_AZURE_ACCOUNT_KEY")
AZURE_ACCOUNT_NAME = env("DJANGO_AZURE_ACCOUNT_NAME")
AZURE_CONTAINER = env("DJANGO_AZURE_CONTAINER_NAME")

STORAGES["default"] = {"BACKEND": "storages.backends.azure_storage.AzureStorage"}
{% endif -%}

