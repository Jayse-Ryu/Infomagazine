from .base import *

DEBUG = False

DEBUG_PROPAGATE_EXCEPTIONS = True

INSTALLED_APPS += ['silk']

MIDDLEWARE +=['silk.middleware.SilkyMiddleware']

NOSE_ARGS = [
    '-I=slik'
]

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['localhost']

CORS_ORIGIN_ALLOW_ALL = True

STATIC_URL = 'https://%s/%s/' % ('assets.infomagazine.xyz', 'static')