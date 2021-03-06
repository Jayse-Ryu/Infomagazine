import os
from datetime import datetime

from django.conf import settings
from django.middleware import csrf
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.serializers import TokenObtainSlidingSerializer, TokenObtainPairSerializer, \
    TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView, TokenObtainPairView, \
    TokenRefreshView, TokenViewBase

from v1.serializers import CustomTokenObtainSlidingSerializer, CustomTokenRefreshSlidingSerializer


class _CommonSlidingTokenView(TokenViewBase):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        csrf.get_token(request)

        response_data = serializer.validated_data

        response = Response({"token": response_data.get('token')})

        expiration = (
                datetime.utcnow() + settings.SIMPLE_JWT['SLIDING_TOKEN_LIFETIME']
        )

        if os.getenv('SERVER_TYPE') == "dev":
            response.set_cookie(
                'JWT', response_data.get('token'), expires=expiration, httponly=True
            )

            response.set_cookie(
                'SESSION', response_data.get('session_token'), expires=expiration
            )
        else:
            response.set_cookie(
                'JWT', response_data.get('token'),
                expires=expiration,
                httponly=True,
                domain=settings.CSRF_COOKIE_DOMAIN,
                samesite='Lax',
                secure=True
            )

            response.set_cookie(
                'SESSION', response_data.get('session_token'),
                expires=expiration,
                domain=settings.CSRF_COOKIE_DOMAIN,
                samesite='Lax',
                secure=True
            )

        return response


class CustomTokenObtainSlidingView(_CommonSlidingTokenView, TokenObtainSlidingView):
    serializer_class = CustomTokenObtainSlidingSerializer


custom_token_obtain_sliding = CustomTokenObtainSlidingView.as_view()


class CustomTokenRefreshSlidingView(_CommonSlidingTokenView, TokenRefreshSlidingView):
    serializer_class = CustomTokenRefreshSlidingSerializer


custom_token_refresh_sliding = CustomTokenRefreshSlidingView.as_view()


class CumstomTokenObtainPairView(TokenObtainPairView):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = TokenObtainPairSerializer


custom_token_obtain_pair = TokenObtainPairView.as_view()


class CustomTokenRefreshView(TokenRefreshView):
    """
    Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.
    """
    serializer_class = TokenRefreshSerializer


custom_token_refresh = TokenRefreshView.as_view()
