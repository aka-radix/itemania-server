from datetime import timedelta
from pathlib import Path

import environ

# BASE DIR

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ENV

env = environ.Env()

environ.Env.read_env(BASE_DIR / ".env")


# GENERAL

SITE_ID = 1

SECRET_KEY = env.str("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

APPS_DIR = BASE_DIR / "itemania"

WSGI_APPLICATION = "config.wsgi.application"

ROOT_URLCONF = "config.urls"

AUTH_USER_MODEL = "users.User"

# LOCALIZATION AND INTERNATIONALIZATION

LANGUAGE_CODE = "en-us"

TIME_ZONE = env.str("DJANGO_TIME_ZONE")

USE_I18N = True

USE_TZ = True


# DEFAULT PRIMARY KEY

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# STATIC FILES

STATIC_URL = "/static/"

STATIC_URL = "/static/"

STATICFILES_DIRS = [str(APPS_DIR / "static")]


# MEDIA FILES

MEDIA_ROOT = str(APPS_DIR / "media")

MEDIA_URL = "/media/"


# APPLICATION DEFINITION

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "dj_rest_auth",
    "rest_framework",
    "rest_framework_simplejwt",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth.registration",
    "rest_framework.authtoken",
]

LOCAL_APPS = [
    "itemania.users",
    "itemania.items",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# MIDDLEWARE

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]


# TEMPLATES

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


# DATABASE

DATABASES = {
    "default": env.db("DATABASE_URL"),
}

DATABASES["default"]["ATOMIC_REQUESTS"] = True


# PASSWORD VALIDATORS

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa: E501
    },
]


# REST FRAMEWORK

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "itemania.items.api.paginators.StandardResultsSetPagination",  # noqa: E501
}


# REST AUTH

REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "auth-cookie",
    "JWT_AUTH_REFRESH_COOKIE": "refresh-cookie",
    "REGISTER_SERIALIZER": "itemania.users.api.serializers.UserRegistrationSerializer",  # noqa: E501
    "JWT_AUTH_HTTPONLY": False,
}


# SIMPLE JWT

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=720),
    "UPDATE_LAST_LOGIN": True,
}
