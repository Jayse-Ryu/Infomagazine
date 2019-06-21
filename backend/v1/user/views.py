from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

import v1.permissions as custom_permissions
from infomagazine.custom_packages import CustomModelViewSet
from v1.user.models import User
from v1.user.serializers import UserSerializer, CreateClientSerializer


class UserViewSets(CustomModelViewSet):
    queryset = User.objects.select_related('info').all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['POST'], permission_classes=[custom_permissions.IsMarketer])
    def create_client(self, request):
        serializer = CreateClientSerializer(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        result = {
            'state': True,
            'data': serializer.data,
            'message': 'success'
        }

        return Response(result, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['GET'], permission_classes=[permissions.AllowAny])
    def email_check(self, request):
        get_qs = request.query_params.dict()
        result = {
            'state': False,
            'data':
                {
                    'email_check': False
                },
            'message': 'fail'
        }

        if 'email' not in get_qs:
            result['message'] = 'must set query string "email"'
        else:
            result['state'] = True
            email_check = User.objects.filter(email=get_qs['email'])

            if email_check.exists():
                result['data']['email_check'] = True
                result['message'] = 'Existing email.'
            else:
                result['message'] = 'Nonexistent email.'

        return Response(result, status=status.HTTP_200_OK)

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
