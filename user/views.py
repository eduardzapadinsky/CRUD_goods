from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenViewBase

from .models import UserModel
from .serializers import UserSerializer, TokenSerializer


class UserCreateView(generics.CreateAPIView):
    """
    This view allows users to register by providing a username and password.
    """

    permission_classes = [AllowAny]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class LoginView(TokenViewBase):
    """
    This view allows users to obtain authentication tokens by providing valid credentials.
    """

    serializer_class = TokenSerializer