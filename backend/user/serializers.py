from rest_framework import serializers
from user.models import User, UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('user', 'access_role',)


class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    # user_access_info = UserInfoSerializer()

    class Meta:
        # Specify the model we are using
        model = User
        # Specify the fields that should be made accessible.
        # Mostly it is all fields in that modesl
        fields = ('id', 'email', 'password')

        extra_kwargs = {
            'password':
                {
                    'write_only': True
                },
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        UserInfo.objects.create(user=user)
        return user
