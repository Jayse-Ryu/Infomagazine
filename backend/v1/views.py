from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView

from v1.serializers import CustomTokenObtainSlidingSerializer


class CustomTokenObtainSlidingView(TokenObtainSlidingView):
    serializer_class = CustomTokenObtainSlidingSerializer


custom_token_obtain_sliding = CustomTokenObtainSlidingView.as_view()


class CustomTokenRefreshSlidingView(TokenRefreshSlidingView):
    permission_classes = (permissions.IsAuthenticated,)


custom_token_refresh_sliding = CustomTokenRefreshSlidingView.as_view()
