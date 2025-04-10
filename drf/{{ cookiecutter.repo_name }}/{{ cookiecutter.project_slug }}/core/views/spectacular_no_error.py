import contextlib

from drf_spectacular.utils import extend_schema
from drf_spectacular.views import SpectacularAPIView


@contextlib.contextmanager
def alter_error_schema():
    from drf_standardized_errors.openapi import AutoSchema

    old_schema_should_add_error_response = AutoSchema._should_add_error_response  # noqa

    def new_schema_should_add_error_response(self, responses: dict, status_code: str):
        return False

    try:
        AutoSchema._should_add_error_response = new_schema_should_add_error_response
        yield
    finally:
        AutoSchema._should_add_error_response = old_schema_should_add_error_response


class SpectacularNoErrorAPIView(SpectacularAPIView):
    """
    Custom API view that generates schema documentation without error responses.

    This view extends SpectacularAPIView to produce a schema that excludes error definitions,
    which is useful for API-based code generation. By omitting repetitive error schemas,
    the generated documentation remains concise and more manageable in size.
    """

    @extend_schema(exclude=True)
    def get(self, request, *args, **kwargs):
        with alter_error_schema():
            return super().get(request, *args, **kwargs)
