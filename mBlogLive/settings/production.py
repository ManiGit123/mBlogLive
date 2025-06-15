from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv("USERNAME") == "manik":
    print("debug is True -----------", os.getenv("USERNAME"))
    DEBUG = True
elif os.environ.get("MY_USERNAME") == "manirender":
    print(
        "debug is False -----------",
        "render environ read success",
        os.environ.get("USERNAME"),
    )
    DEBUG = False
else:
    print("debug is False -----------", os.getenv("USERNAME"))
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
