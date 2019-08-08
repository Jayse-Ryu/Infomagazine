from infomagazine.utils import DefaultRouter
from v1.user.views import UserViewSets

router = DefaultRouter()
router.register(r'users', UserViewSets, basename='user')
