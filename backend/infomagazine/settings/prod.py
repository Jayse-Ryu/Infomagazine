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

SECURE_BROWSER_XSS_FILTER = True

SECURE_SSL_REDIRECT = True

X_FRAME_OPTIONS = "DENY"

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_HSTS_SECONDS = 60

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

STATIC_URL = f"""https://{os.getenv('STATIC_URL')}/static/"""

# CORS_ALLOW_CREDENTIALS = True
#
# SESSION_COOKIE_SAMESITE = 'Strict'
# CSRF_COOKIE_SAMESITE = 'Strict'

# SESSION_COOKIE_SAMESITE = None

# CSRF_COOKIE_NAME = 'XSRF-TOKEN'
#
# CSRF_HEADER_NAME = 'HTTP_X_XSRF_TOKEN'
#
# CORS_ALLOW_HEADERS = (
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-xsrf-token',
#     'x-requested-with',
# )

# TODO prod상에서 꼭 명시 - 서브도메인 지원을 위해
# CSRF_COOKIE_DOMAIN = os.getenv('CSRF_COOKIE_DOMAIN')

# CORS_ORIGIN_WHITELIST = tuple(os.getenv('CORS_ORIGIN_WHITELIST', cast=Csv()))
# CSRF_TRUSTED_ORIGINS = tuple(os.getenv('CSRF_TRUSTED_ORIGINS', cast=Csv()))
