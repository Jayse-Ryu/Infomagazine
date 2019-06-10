from django.urls import path

from user.views import UserListCreateAPIView, UserRetrieveUpdate

app_name = 'user'
urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='list'),
    path('<int:pk>/', UserRetrieveUpdate.as_view(), name='detail'),
]
