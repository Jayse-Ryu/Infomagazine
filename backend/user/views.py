from rest_framework import generics, permissions

# Create your views here.
from user.models import User
from user.serializers import UserSerializer, UserCreateSerializer


# https://gist.github.com/codephillip/03ff3831d0ada36663bed0cc7c4bba0b
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        return UserCreateSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve a user or update user information.
    Accepts GET and PUT requests and the record id must be provided in the request """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
