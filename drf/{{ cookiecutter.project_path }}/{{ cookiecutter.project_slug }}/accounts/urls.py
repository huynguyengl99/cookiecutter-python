from django.urls import include, path, re_path

from dj_rest_auth.registration.views import VerifyEmailView

{%- if cookiecutter.camelize_api %}
from accounts.views.detail_view import UserDetailsView
{%- endif %}
{%- if cookiecutter.google_login %}
from accounts.views.google_login_view import GoogleLogin
{%- endif %}
from accounts.views.logout_view import LogoutView

urlpatterns = [
    re_path(
        r"^registration/account-confirm-email/(?P<key>[-:\w]+)/$",
        VerifyEmailView.as_view(),
        name="account_confirm_email",
    ),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("logout/", LogoutView.as_view(), name="custom_rest_logout"),
{%- if cookiecutter.camelize_api %}
    path("user/", UserDetailsView.as_view(), name="custom_rest_user_details"),
{%- endif %}
{%- if cookiecutter.google_login %}
    path("login/google/", GoogleLogin.as_view(), name="google_login"),
{%- endif %}
    path("", include("dj_rest_auth.urls")),
]
