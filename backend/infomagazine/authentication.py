from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomJWTAuthentication(JWTAuthentication, SessionAuthentication):
    def authenticate(self, request):

        get_authenticate = super().authenticate(request)

        self.enforce_csrf(request)

        return get_authenticate
