from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductByCategoryView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_name = self.kwargs['category']
        category = Category.objects.get(name=category_name)
        return Product.objects.filter(category=category)
