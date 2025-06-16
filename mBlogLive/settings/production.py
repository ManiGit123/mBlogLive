from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
renderUsername = os.environ.get("MY_USERNAME")
if os.getenv("USERNAME") == "manik":
    print("debug is True -----------", os.getenv("USERNAME"))
    DEBUG = True
elif renderUsername == "manirender":
    print(
        "debug is False -----------",
        "render environ read success",
        os.environ.get("USERNAME"),
    )
    DEBUG = False
else:
    print("debug is False -----------", os.getenv("MY_USERNAME"))
    DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1:8000", "*"]
CSRF_TRUSTED_ORIGINS = ["https://mbloglive.onrender.com"]

try:
    from .local import *
except ImportError:
    pass


if not DEBUG:
    # whitenoise setup
    # WHITENOISE_MANIFEST_STRICT = False
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATIC_URL = "/static/"
    STORAGES = {
        "default": {
            "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }
    if (
        os.environ.get("CLOUD_NAME")
        and os.environ.get("API_KEY")
        and os.environ.get("API_SECRET")
    ):
        print("cloudinary env var works fine!............")
        CLOUDINARY_STORAGE = {
            "CLOUD_NAME": os.environ.get("CLOUD_NAME"),
            "API_KEY": os.environ.get("API_KEY"),
            "API_SECRET": os.environ.get("API_SECRET"),
        }
if not DEBUG:
    import logging

    logging.basicConfig(level=logging.DEBUG)
