import requests

from infomagazine.utils import split_env
from .base import *

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = split_env(os.getenv('ALLOWED_HOSTS'))

DEBUG = False

# EC2_PRIVATE_IP = None
# try:
#     EC2_PRIVATE_IP = requests.get(
#         'http://169.254.169.254/latest/meta-data/local-ipv4',
#         timeout=0.01).text
# except requests.exceptions.RequestException:
#     pass
#
# if EC2_PRIVATE_IP:
#     ALLOWED_HOSTS.append(EC2_PRIVATE_IP)


CORS_ORIGIN_WHITELIST = split_env(os.getenv('CORS_ORIGIN_WHITELIST'))

CSRF_TRUSTED_ORIGINS = split_env(os.getenv('CSRF_TRUSTED_ORIGINS'))

CSRF_COOKIE_DOMAIN = os.getenv('CSRF_COOKIE_DOMAIN')

SECURE_BROWSER_XSS_FILTER = True

SECURE_SSL_REDIRECT = True

X_FRAME_OPTIONS = "DENY"

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_HSTS_SECONDS = 60

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

CSRF_COOKIE_SECURE = True

CORS_ALLOW_CREDENTIALS = True