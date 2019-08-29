from datetime import datetime

from django.conf import settings
from django.forms import model_to_dict
from rest_framework_simplejwt.serializers import TokenObtainSlidingSerializer


class CustomTokenObtainSlidingSerializer(TokenObtainSlidingSerializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, attrs):
        data = super().validate(attrs)

        token = self.get_token(self.user)

        data['token'] = str(token)

        session_token = self.get_token(self.user)
        user_info_dict = model_to_dict(self.user.info)
        session_token['id'] = self.user.id
        session_token['email'] = self.user.email
        session_token['username'] = self.user.username
        session_token['is_superuser'] = self.user.is_superuser
        session_token['is_staff'] = self.user.is_staff
        session_token['access_role'] = user_info_dict['access_role']
        expiration = str(datetime.utcnow() + settings.SIMPLE_JWT['SLIDING_TOKEN_LIFETIME'])
        session_token['expired_data'] = expiration

        data['session_token'] = str(session_token)

        data['expired_data'] = expiration

        return data
