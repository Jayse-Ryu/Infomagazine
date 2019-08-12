from rest_framework import permissions

import v1.permissions as custom_permissions
from v1.company.models import Company
from v1.company.serializers import CompanySerializer
from infomagazine.custom_packages import CustomModelViewSet


class CompanyViewSets(CustomModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            request = self.request

            get_qs = request.query_params.dict()

            filter_fields = {
                'users__info__organization_id': request.user.info.organization_id,
                'users__info__access_role__in': [0, 1]
            }

            if 'detail' in get_qs:
                del get_qs['detail']
                filter_fields.update({'users__id': request.user.id})

            filter_fields.update({key + "__contains": value for key, value in get_qs.items()})

            return self.queryset.filter(**filter_fields)
        return self.queryset.all()

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [custom_permissions.IsClient]
        else:
            permission_classes = [custom_permissions.IsMarketer]
        return [permission() for permission in permission_classes]
