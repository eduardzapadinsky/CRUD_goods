"""
URL configuration for goods app.
"""

from django.urls import path

from . import views

app_name = "goods"
urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),

    path('goods/', views.ProductListView.as_view(), name='goods-list'),
    path('goods/<int:pk>/', views.ProductDetailView.as_view(), name='goods-detail'),
    path('goods/category/<str:category>/', views.ProductByCategoryView.as_view(), name='goods-by-category'),

    path('goods/offer-of-the-month/', views.OfferOfMonthView.as_view(), name='products-offer-of-the-month'),
    path('goods/availability/', views.AvailabilityView.as_view(), name='available-products'),
    path('goods/pickup/', views.PickupView.as_view(), name='pickup-products'),
]
