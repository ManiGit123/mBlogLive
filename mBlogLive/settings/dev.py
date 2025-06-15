from .base import *
import os

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

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-gq)krl@u9^7$pfal*))^d=*--e*ha9aua9a%q7)dr53$37vh&u"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["127.0.0.1:8000", "*"]
CSRF_TRUSTED_ORIGINS = ["https://mbloglive.onrender.com"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


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

if not DEBUG:
    import logging

    logging.basicConfig(level=logging.DEBUG)
