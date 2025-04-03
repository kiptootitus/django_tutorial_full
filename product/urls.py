from django.urls import path
from product.views import ProductDetailAPIView, ProductListAPIView, ProductListCreateAPIView, ProductUpdateAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view(), name= 'product_view'),
    path('detail/<int:pk>/', ProductDetailAPIView.as_view(), name='product_detail'),
    path('create/', ProductListCreateAPIView.as_view(), name='product_create'),

]
