from .base import *  # noqa: F403
from .base import INSTALLED_APPS, MIDDLEWARE

# GENERAL

DEBUG = True


# APPS

INSTALLED_APPS += ["silk", "django_extensions"]


# MIDDLEWARE

MIDDLEWARE += ["silk.middleware.SilkyMiddleware"]


# SILK

SILKY_PYTHON_PROFILER = True

SILKY_META = True
