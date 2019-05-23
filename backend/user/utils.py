from user.serializers import UserAuthReturnSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserAuthReturnSerializer(user, context={'request': request}).data
    }
