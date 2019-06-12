from rest_framework import generics, viewsets

from infomagazine import permissions as custom_permissions
from company.models import Company
from company.serializers import CompanySerializer


class CompanyViewSets(viewsets.ModelViewSet):
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

            if 'limit' in get_qs:
                limit = get_qs.pop('limit')

            if 'offset' in get_qs:
                offset = get_qs.pop('offset')

            if 'detail' in get_qs:
                del get_qs['detail']
                filter_fields.update({'users__id': request.user.id})

            filter_fields.update({key + "__contains": value for key, value in get_qs.items()})

            return self.queryset.filter(**filter_fields)
        return self.queryset.all()

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'partial_update']:
            return [custom_permissions.IsClient()]
        return [custom_permissions.IsMarketer()]


# class CompanyListCreateAPIView(generics.ListCreateAPIView):
#     permission_classes = (custom_permissions.IsMarketer,)
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#
#     def get_queryset(self):
#         if self.request.method == 'GET':
#             request = self.request
#
#             get_qs = request.query_params.dict()
#
#             filter_fields = {
#                 'users__info__organization_id': request.user.info.organization_id,
#                 'users__info__access_role__in': [0, 1]
#             }
#
#             if 'limit' in get_qs:
#                 limit = get_qs.pop('limit')
#
#             if 'offset' in get_qs:
#                 offset = get_qs.pop('offset')
#
#             if 'detail' in get_qs:
#                 del get_qs['detail']
#                 filter_fields.update({'users__id': request.user.id})
#
#             filter_fields.update({key + "__contains": value for key, value in get_qs.items()})
#
#             return self.queryset.filter(**filter_fields)
#         return self.queryset.all()
#
#
# class CompanyRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#
#     def get_permissions(self):
#         if self.request.method in ['GET', 'PUT']:
#             return [custom_permissions.IsClient()]
#         return [custom_permissions.IsMarketer()]
