from django.shortcuts import render
from rest_framework import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework import permissions, authentication,status
from rest_framework.views import APIView

from rest_framework.response import Response

class ProductListAPIView(generics.ListAPIView):
    """
    View to list all products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def get_queryset(self):

        return Product.objects.all()

    

      

class ProductUpdateAPIView(generics.UpdateAPIView):
    """
    This will update the product per selected id
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @method_decorator(cache_page(60 * 5))  # Cache the response for 5 minutes
    def get_queryset(self, request, *args, **kwargs):
        qs = super().get_queryset(**args, **kwargs)
        request = self.request
        user = request.user
        
        if not user.is_authenticated:
            return Product.objects.none()
        
        return qs.filter(user=request.user)  # Fetch all products
    

      
    def update(self, request, *args, **kwargs):

      partial = kwargs.pop('partial', False)  # Check if it's a partial update (PATCH)
      instance = self.get_object()  # Get the product instance by ID

      # Remove 'vendor' from the request data if it exists
      request_data = request.data.copy()

      serializer = self.get_serializer(instance, data=request_data, partial=partial)
      serializer.is_valid(raise_exception=True)
      self.perform_update(serializer)
      return Response(serializer.data, status=status.HTTP_200_OK)
  
  
  
  
class ProductDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @method_decorator(cache_page(60 * 5))  # Cache the response for 5 minutes
    def get(self, request, *args, **kwargs):
        # Get the single product based on the pk from the URL
        product = self.get_object()  # This fetches the object by pk automatically
        serializer = self.serializer_class(product, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
class ProductListCreateAPIView(generics.CreateAPIView):
    queryset  = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
    def get_queryset(self, request, *args, **kwargs):
        qs = super().get_queryset(**args, **kwargs)
        request = self.request
        user = request.user
        
        if not user.is_authenticated:
            return Product.objects.none()
        
        return qs.filter(user=request.user)  # Fetch all products
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    
    