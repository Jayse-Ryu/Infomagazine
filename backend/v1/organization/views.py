from rest_framework import permissions

import v1.permissions as custom_permissions
from infomagazine.custom_packages import CustomModelViewSet
from v1.organization.filters import OrganizationFilter
from v1.organization.models import Organization
from v1.organization.serializers import OrganizationSerializer


class OrganizationViewSets(CustomModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filterset_class = OrganizationFilter

    def get_permissions(self):
        if self.action in ['list']:
            return [permissions.IsAdminUser()]
        elif self.action in ['retrieve']:
            return [custom_permissions.IsMarketer()]
        return [permissions.IsAdminUser()]
