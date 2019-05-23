from django.urls import path

from user.views import UserList, UserCreate, UserRetrieveUpdate

urlpatterns = [
    path('', UserList.as_view()),
    path('create/', UserCreate.as_view()),
    path('<int:pk>/', UserRetrieveUpdate.as_view()),
]
