"""
URL configuration for user app.
"""

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserCreateView, LoginView

app_name = "user"
urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='user_signup'),
    path('auth/', LoginView.as_view(), name='token_obtain_pair'),
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
