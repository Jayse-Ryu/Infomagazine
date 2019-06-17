from django.urls import path

from organization.views import OrganizationListCreateAPIView, OrganizationRetrieveUpdateAPIView

app_name = 'organization'
urlpatterns = [
    path('', OrganizationListCreateAPIView.as_view()),
    path('<int:pk>', OrganizationRetrieveUpdateAPIView.as_view()),
]
