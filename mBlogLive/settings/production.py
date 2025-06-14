from .base import *

DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1:8000", "*"]
CSRF_TRUSTED_ORIGINS = ["https://mbloglive.onrender.com"]

try:
    from .local import *
except ImportError:
    pass


if not DEBUG:
    # whitenoise setup
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
