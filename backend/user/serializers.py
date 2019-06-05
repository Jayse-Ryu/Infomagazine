from django.forms import model_to_dict
from rest_framework import serializers

from company.models import Company
from user.models import User, UserInfo, AccessRole


# class UserInfoSerializer(serializers.ModelSerializer):
#     organization = serializers.SerializerMethodField(read_only=True)
#     company = serializers.SerializerMethodField(read_only=True)
#
#     def get_organization(self, obj):
#         if obj.organization:
#             return model_to_dict(obj.organization)
#         else:
#             return None
#
#     def get_company(self, obj):
#         if obj.user.company_set.exists():
#             return [query_set for query_set in iter(
#                 obj.user.company_set.values('id', 'corp_name', 'corp_sub_name', 'corp_header', 'corp_address',
#                                             'corp_num',
#                                             'corp_desc').all()
#             )]
#         else:
#             return None
#
#     class Meta:
#         model = UserInfo
#         fields = ('access_role', 'phone_num', 'updated_date', 'organization', 'company',)

# class UserAuthReturnSerializer(serializers.ModelSerializer):
#     info = UserInfoSerializer(read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('id', 'email', 'password', 'username', 'is_superuser', 'is_staff', 'is_active', 'info', 'last_login',
#                   'date_joined',)
#
#         extra_kwargs = {
#             'password':
#                 {
#                     'write_only': True
#                 },
#         }

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


class UserInfoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('phone_num',)


class UserCreateSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """

    info = UserInfoCreateSerializer()

    class Meta:
        # Specify the model we are using
        model = User
        # Specify the fields that should be made accessible.
        # Mostly it is all fields in that modesl
        # fields = ('email', 'password', 'username', 'phone_num',)
        fields = ('email', 'password', 'username', 'info',)
        # related_fields = ['info']

        extra_kwargs = {
            'password':
                {
                    'write_only': True
                },
        }

    # phone_num = serializers.CharField(source='info.phone_num')

    def validate(self, data):
        """
        1. register_type이 company일 경우 반드시 company_id를 설정해야만 한다.
        2. 해당 company가 존재해야 한다.
        """
        request = self.context['request']
        get_qs = request.query_params.dict()
        if 'register_type' in get_qs:
            register_type = get_qs.pop('register_type')
            if register_type == 'company':
                if 'company_id' not in get_qs:
                    raise serializers.ValidationError("You must set 'company_id'.")
                else:
                    company_id = get_qs.pop('company_id')
                    company_check = Company.objects.filter(id=company_id)
                    if not company_check.exists():
                        raise serializers.ValidationError("The company does not exist.")
        return data

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        user_info_column = {
            'user': user,
            'phone_num': validated_data['info']['phone_num']
        }

        request = self.context['request']
        get_qs = request.query_params.dict()
        if 'register_type' in get_qs:
            register_type = get_qs.pop('register_type')
            if register_type == 'company':
                user_info_column.update({'access_role': AccessRole.CLIENT,
                                         'organization': request.user.info.organization})
                company_id = get_qs.pop('company_id')
                company = Company.objects.get(id=company_id)
                company.users.add(user)

        UserInfo.objects.create(**user_info_column)

        return user
