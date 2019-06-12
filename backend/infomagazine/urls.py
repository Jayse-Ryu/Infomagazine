"""apiserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from company.views import CompanyViewSets
from infomagazine.views import custom_token_obtain_sliding, custom_token_refresh_sliding
from organization.views import OrganizationViewSets
from user.views import UserViewSets

api_patterns = ([
                    path('auth/', custom_token_obtain_sliding, name='token_obtain_sliding'),
                    path('auth/refresh/', custom_token_refresh_sliding, name='token_refresh_sliding'),
                    # path('organizations/', include('organization.urls', namespace='organizations')),
                    # path('companies/', include('company.urls', namespace='companies')),
                ], 'v1')

router = DefaultRouter()
router.register(r'users', UserViewSets, basename='users')
router.register(r'organizations', OrganizationViewSets, basename='organizations')
router.register(r'companies', CompanyViewSets, basename='companies')
api_patterns[0].extend(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/v1/', include(api_patterns, namespace='v1'))
]

if settings.DEBUG:
    from silk import urls
    from rest_framework_swagger.views import get_swagger_view

    schema_view = get_swagger_view(title='Infomagzine API')

    urlpatterns.extend([
        path('silk/', include(urls, namespace='silk')),
    ])

    api_patterns[0].extend([
        path('swagger/', schema_view, name='swagger'),
    ])
