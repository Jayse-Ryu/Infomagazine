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

from infomagazine.views import custom_token_obtain_sliding, custom_token_refresh_sliding

api_patterns = ([
                    path('auth/', custom_token_obtain_sliding, name='token_obtain_sliding'),
                    path('auth/refresh/', custom_token_refresh_sliding, name='token_refresh_sliding'),
                    path('user/', include('user.urls', namespace='user')),
                    path('organization/', include('organization.urls', namespace='organization')),
                    path('company/', include('company.urls', namespace='company')),
                ], 'v1')

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
        path('swagger/', schema_view, name='swagger'),
    ])
