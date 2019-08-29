from random import randint

import jwt
from django.conf import settings
from django.forms import model_to_dict
from rest_framework import serializers, exceptions
from rest_framework_simplejwt.serializers import TokenObtainSlidingSerializer, TokenRefreshSlidingSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import SlidingToken


def _session_token_generator(user_info=None, exp=None):
    payload = {}

    if isinstance(user_info, dict):
        payload['exp'] = exp
        payload['id'] = user_info['id']
        payload['email'] = user_info['email']
        payload['username'] = user_info['username']
        payload['is_superuser'] = user_info['is_superuser']
        payload['is_staff'] = user_info['is_staff']
        payload['access_role'] = user_info['access_role']
    else:
        payload['exp'] = exp
        payload['id'] = user_info.id
        payload['email'] = user_info.email
        payload['username'] = user_info.username
        payload['is_superuser'] = user_info.is_superuser
        payload['is_staff'] = user_info.is_staff
        user_info_dict = model_to_dict(user_info.info)
        payload['access_role'] = user_info_dict['access_role']
        payload['rand_id'] = randint(0, 1000)

    session_token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm='HS256')
    return session_token.decode('utf-8')


class CustomTokenObtainSlidingSerializer(TokenObtainSlidingSerializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, attrs):
        data = super().validate(attrs)

        token = self.get_token(self.user)

        data['token'] = str(token)

        generated_token = jwt.decode(str(token).encode('utf-8'), settings.SECRET_KEY)

        data['session_token'] = str(_session_token_generator(self.user, exp=generated_token['exp']))

        return data


class CustomTokenRefreshSlidingSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        requested_cookies = self.context['request'].COOKIES

        try:
            token = SlidingToken(requested_cookies['JWT'])
        except Exception:
            raise exceptions.APIException("Invalid token")

        # Check that the timestamp in the "refresh_exp" claim has not
        # passed
        token.check_exp(api_settings.SLIDING_TOKEN_REFRESH_EXP_CLAIM)

        # Update the "exp" claim
        token.set_exp()

        refreshed_token = jwt.decode(str(token).encode('utf-8'), settings.SECRET_KEY)
        requested_refresh_token = jwt.decode(requested_cookies['SESSION'].encode('utf-8'), settings.SECRET_KEY)

        return {'token': str(token), 'session_token': str(
            _session_token_generator(user_info=requested_refresh_token, exp=refreshed_token['refresh_exp']))}
