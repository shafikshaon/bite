from pathlib import Path

from decouple import config

from .config import DATABASES  # noqa
from .config import apps  # noqa
from .config import auth  # noqa
from .config import email  # noqa
from .config import internationalization  # noqa
from .config import middleware  # noqa
from .config import security  # noqa
from .config import staticfiles  # noqa
from .config import templates  # noqa

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-l*)*od$+nvs67tc7$!95$0dla2gb3o9i@kp+ncr#b(vhu9361q",
)

DEBUG = config("DEBUG", cast=bool)

ALLOWED_HOSTS = []

THIRD_PARTY_APPS = []

INSTALLED_APPS = THIRD_PARTY_APPS + apps.DJANGO_DEFAULT_APPS + apps.CUSTOM_APPS

ROOT_URLCONF = "bite.urls"

WSGI_APPLICATION = "bite.wsgi.application"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
