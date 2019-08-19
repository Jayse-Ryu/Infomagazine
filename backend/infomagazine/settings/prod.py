# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURE_BROWSER_XSS_FILTER = True

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
