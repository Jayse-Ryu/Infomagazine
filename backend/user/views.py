from rest_framework import generics, permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from infomagazine import permissions as custom_permissions
from user.models import User
from user.serializers import UserSerializer, CreateClientSerializer


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create', 'email_check']:
            return [permissions.AllowAny()]
        elif self.action in ['update', 'partial_update']:
            return [permissions.IsAuthenticated()]
        elif self.action in ['create_client']:
            return [custom_permissions.IsMarketer()]
        return [permissions.IsAdminUser()]

    def get_serializer_context(self):
        context = {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

        if self.action not in ['create', 'create_client', 'list'] and 'pk' in self.kwargs:
            context.update({'pk': self.kwargs['pk']})

        return context

    @action(detail=False, methods=['POST'], permission_classes=[custom_permissions.IsMarketer])
    def create_client(self, request):
        serializer = CreateClientSerializer(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['GET'], permission_classes=[permissions.AllowAny])
    def email_check(self, request):
        get_qs = request.query_params.dict()
        email_check = User.objects.filter(email=get_qs['email'])
        result = {'data': {'email_check': False}}
        if email_check.exists():
            setattr(result, 'data', {'email_check': True})

        return Response(result, status=status.HTTP_200_OK)

    # @action()
    # def test(self,request):

#
# class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
#     """ Retrieve a user or update user information.
#     Accepts GET and PUT requests and the record id must be provided in the request """
#
#     def get_queryset(self):
#         queryset = User.objects.get(pk=self.request.user.id)
#         return queryset
#
#     def get_serializer_class(self):
#         if self.request.method == 'PATCH':
#             get_qs = self.request.query_params.dict()
#             if 'fields' in get_qs:
#                 return UserOrganizationSerializer
#         return UserSerializer
#
#     def get_permissions(self):
#         if self.request.method == 'PATCH':
#             get_qs = self.request.query_params.dict()
#             if 'fields' in get_qs:
#                 return [custom_permissions.IsOnlyGuest(), permissions.IsAdminUser()]
#         return [permissions.IsAuthenticated()]
#
#     def check_permissions(self, request):
#         """
#         Check if the request should be permitted.
#         Raises an appropriate exception if the request is not permitted.
#         """
#         check_permission = False
#         permission = None
#         for permission in self.get_permissions():
#             if permission.has_permission(request, self):
#                 check_permission = True
#             else:
#                 permission = permission
#
#         if not check_permission:
#             self.permission_denied(
#                 request, message=getattr(permission, 'message', None)
#             )
