from rest_framework import permissions

from infomagazine import permissions as custom_permissions
from infomagazine.custom import CustomModelViewSet
from organization.filters import OrganizationFilter
from organization.models import Organization
from organization.serializers import OrganizationSerializer


class OrganizationViewSets(CustomModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filterset_class = OrganizationFilter

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [custom_permissions.IsGuest()]
        return [permissions.IsAdminUser()]
