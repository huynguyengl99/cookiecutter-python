from django.urls import include, path

{%- if cookiecutter.camelize_api %}
from accounts.views.detail_view import UserDetailsView
{%- endif %}
{%- if cookiecutter.google_login %}
from accounts.views.google_login_view import GoogleLogin
{%- endif %}
from accounts.views.logout_view import LogoutView

urlpatterns = [
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
{%- if cookiecutter.camelize_api %}
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
{%- endif %}
{%- if cookiecutter.google_login %}
    path("login/google/", GoogleLogin.as_view(), name="google_login"),
{%- endif %}
    path("", include("dj_rest_auth.urls")),
]
