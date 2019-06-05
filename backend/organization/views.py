from rest_framework import generics, permissions

from infomagazine import permissions as custom_permissions
from organization.models import Organization
from organization.serializers import OrganizationSerializer


class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            get_qs = self.request.query_params.dict()
            if 'limit' in get_qs:
                limit = get_qs.pop('limit')

            if 'offset' in get_qs:
                offset = get_qs.pop('offset')

            filter_fields = {key + "__contains": value for key, value in get_qs.items()}
            return self.queryset.filter(**filter_fields)
        return self.queryset.all()


class OrganizationRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (custom_permissions.IsOwner,)
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
