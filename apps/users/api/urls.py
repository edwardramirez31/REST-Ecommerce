from django.urls import path

from .api import UserAPIView, user_api_view, users_api_view

urlpatterns = [
    path('', UserAPIView.as_view(), name="users_api"),
    path('users/', users_api_view, name="function_api"),
    path('user/<int:pk>', user_api_view, name="user_api"),
]