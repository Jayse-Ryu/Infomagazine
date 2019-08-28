from datetime import datetime

from django.conf import settings
from django.middleware import csrf
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.serializers import TokenObtainSlidingSerializer
from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView

from v1.serializers import CustomTokenObtainSlidingSerializer


class CustomTokenObtainSlidingView(TokenObtainSlidingView):
    serializer_class = CustomTokenObtainSlidingSerializer
    # serializer_class = TokenObtainSlidingSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        csrf.get_token(request)

        expiration = (
                datetime.now() + settings.SIMPLE_JWT['SLIDING_TOKEN_LIFETIME']
        )

        response_data = serializer.validated_data
        response = Response(response_data)
        response.set_cookie(
            'JWT', serializer.validated_data.get('token'), expires=expiration,
            httponly=True, samesite='Lax'
        )

        return response


custom_token_obtain_sliding = CustomTokenObtainSlidingView.as_view()


class CustomTokenRefreshSlidingView(TokenRefreshSlidingView):
    permission_classes = (permissions.IsAuthenticated,)


custom_token_refresh_sliding = CustomTokenRefreshSlidingView.as_view()
