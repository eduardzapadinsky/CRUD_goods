from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class BaseAPIView(generics.GenericAPIView):
    """
    Base API view class that enforces authentication using the IsAdminUser permission.
    """

    permission_classes = [IsAdminUser]


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


class BaseCategoryQueryView(BaseAPIView):
    """
    Base view for querying products by a specific category.
    """

    category_field = None  # Subclasses should define this field (e.g., 'offer_of_the_month', 'availability', 'pickup')

    def get_queryset(self):
        return Product.objects.filter(**{self.category_field: True})

    def get(self, request):
        products = self.get_queryset()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class OfferOfMonthView(BaseCategoryQueryView):
    """
    View for querying products that are marked as 'Offer of the month'
    """

    category_field = 'offer_of_the_month'


class AvailabilityView(BaseCategoryQueryView):
    """
    View for querying available products
    """

    category_field = 'availability'


class PickupView(BaseCategoryQueryView):
    """
    View for querying products available for pickup
    """

    category_field = 'pickup'
