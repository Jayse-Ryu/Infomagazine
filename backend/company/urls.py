from django.urls import path

from company.views import CompanyListCreateAPIView, CompanyRetrieveUpdateAPIView

app_name = 'company'
urlpatterns = [
    path('', CompanyListCreateAPIView.as_view()),
    path('<int:pk>', CompanyRetrieveUpdateAPIView.as_view()),
]
