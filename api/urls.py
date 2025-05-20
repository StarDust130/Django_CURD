

from django.urls import path
from .views import product_list, index, product_detail

urlpatterns = [
    path("", index, name="index"),
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
  
]

