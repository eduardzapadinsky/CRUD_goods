from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenViewBase

from .models import UserModel
from .serializers import UserSerializer, TokenSerializer


class UserCreateView(generics.CreateAPIView):
    """
    This endpoint allows anyone to create a new user account. The new user will be assigned the `is_staff` permission.
    """

    permission_classes = [AllowAny]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(is_staff=True)


class LoginView(TokenViewBase):
    """
    This view allows users to obtain authentication tokens by providing valid credentials.
    """

    serializer_class = TokenSerializer
