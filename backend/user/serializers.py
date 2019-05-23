from django.forms import model_to_dict
from rest_framework import serializers
from user.models import User, UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    organization = serializers.SerializerMethodField(read_only=True)
    company = serializers.SerializerMethodField(read_only=True)

    def get_organization(self, obj):
        if obj.organization:
            return model_to_dict(obj.organization)
        else:
            return None

    def get_company(self, obj):
        if obj.user.company_set.exists():
            return [query_set for query_set in iter(
                obj.user.company_set.values('id', 'corp_name', 'corp_sub_name', 'corp_header', 'corp_address',
                                            'corp_num',
                                            'corp_desc').all()
            )]
        else:
            return None

    class Meta:
        model = UserInfo
        fields = ('access_role', 'phone_num', 'updated_date', 'organization', 'company',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username',)

        extra_kwargs = {
            'password':
                {
                    'write_only': True
                },
        }


class UserAuthReturnSerializer(serializers.ModelSerializer):
    info = UserInfoSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username', 'is_superuser', 'is_staff', 'is_active', 'info', 'last_login',
                  'date_joined',)

        extra_kwargs = {
            'password':
                {
                    'write_only': True
                },
        }


class UserCreateSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """

    class Meta:
        # Specify the model we are using
        model = User
        # Specify the fields that should be made accessible.
        # Mostly it is all fields in that modesl
        fields = ('id', 'email', 'password',)

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
