"""
URL configuration for CRUD_goods project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include("user.urls", namespace="user")),
    path('api/', include("goods.urls", namespace="goods")),
]
