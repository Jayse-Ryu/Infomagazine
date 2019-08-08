from infomagazine.utils import DefaultRouter
from v1.organization.views import OrganizationViewSets

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSets, basename='organization')
