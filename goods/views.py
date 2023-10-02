from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class BaseAPIView(generics.GenericAPIView):
    """
    Base API view class that enforces authentication using the IsAuthenticated permission.
    """

    permission_classes = [IsAuthenticated]


class CategoryListView(BaseAPIView, generics.ListCreateAPIView):
    """
    View for listing and creating Category instances.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(BaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a specific Category instance.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(BaseAPIView, generics.ListCreateAPIView):
    """
    View for listing and creating Product instances.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(BaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a specific Product instance.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductByCategoryView(BaseAPIView, generics.ListAPIView):
    """
    View for listing Product instances by category.
    """

    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        Retrieve a filtered queryset of Product instances based on the specified category.
        """

        category_name = self.kwargs['category']

        try:
            category = Category.objects.get(category_name=category_name)
            return Product.objects.filter(category=category)
        except ObjectDoesNotExist:
            return Product.objects.none()
