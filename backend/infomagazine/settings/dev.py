from .base import *

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['localhost']

DEBUG = True

DEBUG_PROPAGATE_EXCEPTIONS = True

INSTALLED_APPS += ['silk']

MIDDLEWARE += ['silk.middleware.SilkyMiddleware']

NOSE_ARGS = [
    '-I=slik'
]

# CORS_ORIGIN_ALLOW_ALL = True


STATIC_URL = 'https://%s/%s/' % ('assets.infomagazine.xyz', 'static')

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080'
]
