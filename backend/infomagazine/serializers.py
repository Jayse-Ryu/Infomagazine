from django.forms import model_to_dict
from rest_framework_simplejwt.serializers import TokenObtainSlidingSerializer


class CustomTokenObtainSlidingSerializer(TokenObtainSlidingSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        user_info = user.info
        user_info_dict = model_to_dict(user_info)
        user_organization = user_info.organization

        token['id'] = user.id
        token['email'] = user.email
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff
        token['access_role'] = user_info_dict['access_role']
        # token['last_login'] = str(user.last_login)
        # token['phone_num'] = user_info_dict['phone_num']
        if user_organization:
            pass

        return token
