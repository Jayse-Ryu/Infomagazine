from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from v1.company.views import CompanyViewSets
from v1.landingpage.views import LandingPageViewSets
from v1.organization.views import OrganizationViewSets
from v1.user.views import UserViewSets
from v1.views import custom_token_obtain_sliding, custom_token_refresh_sliding

router = DefaultRouter()
router.register(r'users', UserViewSets, basename='user')
router.register(r'organizations', OrganizationViewSets, basename='organization')
router.register(r'companies', CompanyViewSets, basename='company')
router.register(r'landing_pages', LandingPageViewSets, basename='landing_page')

api_urlpatterns = ([
                       path('', include((router.urls, 'router'), namespace='router')),
                       path('auth/', custom_token_obtain_sliding, name='token_obtain_sliding'),
                       path('auth/refresh/', custom_token_refresh_sliding, name='token_refresh_sliding')
                   ], 'v1')

if settings.DEBUG:
    from rest_framework_swagger.views import get_swagger_view

    schema_view = get_swagger_view(title='Infomagzine API')
    api_urlpatterns[0].append(path('swagger/', schema_view, name='swagger'))
