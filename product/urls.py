from django.urls import path
from product.views import ProductListAPIView, ProductUpdateAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view(), name= 'product_view')
]
