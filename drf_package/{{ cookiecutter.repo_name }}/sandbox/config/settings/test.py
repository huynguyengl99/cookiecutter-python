from .dev import *  # NOQA

DEBUG = False
TEST = True

MEDIA_URL = "media-testing/"
MEDIA_ROOT = str(BASE_DIR / "media-testing/")

{%- if cookiecutter.use_websocket %}
# =========================================================================
# CHANX CONFIGURATION
# =========================================================================
CHANX = {
    "SEND_COMPLETION": True,
}
{%- endif %}
