from pathlib import Path

import dj_database_url
from decouple import Csv, config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

AUTH_USER_MODEL = "accounts.CustomUser"

DOC_API = config("DOC_API", cast=bool, default=False)

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # APPs
    "jornada_milhas.core",
    "jornada_milhas.accounts",
    #
    "rest_framework",
    "corsheaders",
]

if DOC_API:
    INSTALLED_APPS.append("drf_spectacular")

if DEBUG:
    INSTALLED_APPS.append("django_extensions")

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "jornada_milhas.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "jornada_milhas.wsgi.application"

# Database

default_db_url = "sqlite:///" + str(BASE_DIR / "db.sqlite3")
parse_db = dj_database_url.parse
DATABASES = {"default": config("DATABASE_URL", default=default_db_url, cast=parse_db)}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles/"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "mediafiles/"

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DEFAULT_RENDERER_CLASSES = ["rest_framework.renderers.JSONRenderer"]

if DEBUG:
    DEFAULT_RENDERER_CLASSES.append("rest_framework.renderers.BrowsableAPIRenderer")

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_RENDERER_CLASSES": DEFAULT_RENDERER_CLASSES,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Jornada Milhas",
    "DESCRIPTION": "Api desenvolvida no challenge backend `7` da `Alura`.",
    "VERSION": "0.1.0",
    "COMPONENT_SPLIT_REQUEST": True,
}


CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", cast=Csv())
