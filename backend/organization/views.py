from rest_framework import permissions, viewsets
from rest_framework.response import Response

from infomagazine import permissions as custom_permissions
from organization.filters import OrganizationFilter
from organization.models import Organization
from organization.serializers import OrganizationSerializer


class OrganizationViewSets(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filterset_class = OrganizationFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [custom_permissions.IsGuest()]
        return [permissions.IsAdminUser()]

# class OrganizationListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Organization.objects.all()
#     serializer_class = OrganizationSerializer
#
#     def get_queryset(self):
#         if self.request.method == 'GET':
#             get_qs = self.request.query_params.dict()
#             if 'limit' in get_qs:
#                 limit = get_qs.pop('limit')
#
#             if 'offset' in get_qs:
#                 offset = get_qs.pop('offset')
#
#             filter_fields = {key + "__contains": value for key, value in get_qs.items()}
#             return self.queryset.filter(**filter_fields)
#         return self.queryset.all()
#
#     def get_permissions(self):
#         if self.request.method in ['GET']:
#             return [custom_permissions.IsGuest()]
#         return [permissions.IsAdminUser()]
#
#
# class OrganizationRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset = Organization.objects.all()
#     serializer_class = OrganizationSerializer
#
#     def get_permissions(self):
#         if self.request.method in ['GET']:
#             return [custom_permissions.IsGuest()]
#         return [custom_permissions.IsOwner()]
