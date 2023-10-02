from django.urls import path

import views

app_name = "goods"
urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('goods/', views.ProductListView.as_view(), name='goods-list'),
    path('goods/<int:pk>/', views.ProductDetailView.as_view(), name='goods-detail'),
    path('goods/category/<str:category>/', views.ProductByCategoryView.as_view(), name='goods-by-category'),
]
