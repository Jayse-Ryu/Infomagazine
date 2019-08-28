from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomJWTAuthentication(JWTAuthentication, SessionAuthentication):
    def authenticate(self, request):
        # header = self.get_header(request)
        # if header is None:
        #     return None
        #
        # raw_token = self.get_raw_token(header)
        # if raw_token is None:
        #     return None

        try:
            raw_token = request.COOKIES['JWT']
        except KeyError:
            return None

        validated_token = self.get_validated_token(raw_token)

        user = self.get_user(validated_token)

        self.enforce_csrf(request)

        return user, None
    # def authenticate(self, request):
    #     get_authenticate = super(JWTAuthentication, self).authenticate(request)
    #
    #     self.enforce_csrf(request)
    #
    #     return get_authenticate
