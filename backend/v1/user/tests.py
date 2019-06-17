"""

"""

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from v1.user.models import User, AccessRole


class AuthorizedUsersTests(APITestCase):
    user_data_email = 'testcase@lcventures.kr'
    user_data_username = 'testcase'
    user_data_password = 'testcase'
    user_data_phone_num = '0109999888'

    create_user_url = reverse('v1:router:user-list')
    obtain_token_url = reverse('v1:token_obtain_sliding')

    def setUp(self):
        self.user_data = [
            {
                'email': self.user_data_email + str(index),
                'username': self.user_data_username + str(index),
                'password': self.user_data_password + str(index),
                'info':
                    {
                        'phone_num': self.user_data_phone_num + str(index)
                    }
            }
            for index in range(len(AccessRole.items()) + 2)
        ]

    def __test_create_user(self, dummy_user_num):
        create_user = self.client.post(self.create_user_url,
                                       self.user_data[dummy_user_num],
                                       format='json')
        self.assertEqual(create_user.status_code, status.HTTP_201_CREATED)

    def __test_obtain_token(self):
        obtain_token = self.client.post(self.obtain_token_url,
                                        {'email': self.user_data[AccessRole.OWNER]['email'],
                                         'password': self.user_data[AccessRole.OWNER]['password']},
                                        format='json')
        self.assertEqual(obtain_token.status_code, status.HTTP_200_OK)
        return obtain_token

    def test_get_owner_obtain_token(self):
        self.__test_create_user(AccessRole.OWNER)
        get_user_data = User.objects.get(email=self.user_data[AccessRole.OWNER]['email'])
        get_user_data.info.access_role = AccessRole.OWNER
        get_user_data.info.save()
        obtain_token = self.__test_obtain_token()
        self.assertTrue('token' in obtain_token.data)
        get_owner_jwt_token = obtain_token.data['token']
        return get_owner_jwt_token

    def test_get_marketer_obtain_token(self):
        self.__test_create_user(AccessRole.OWNER)
        get_user_data = User.objects.get(email=self.user_data[AccessRole.OWNER]['email'])
        get_user_data.info.access_role = AccessRole.MARKETER
        get_user_data.info.save()
        obtain_token = self.__test_obtain_token()
        self.assertTrue('token' in obtain_token.data)
        get_marketer_jwt_token = obtain_token.data['token']
        return get_marketer_jwt_token

    def test_get_client_obtain_token(self):
        self.__test_create_user(AccessRole.OWNER)
        get_user_data = User.objects.get(email=self.user_data[AccessRole.OWNER]['email'])
        get_user_data.info.access_role = AccessRole.CLIENT
        get_user_data.info.save()
        obtain_token = self.__test_obtain_token()
        self.assertTrue('token' in obtain_token.data)
        get_client_jwt_token = obtain_token.data['token']
        return get_client_jwt_token
