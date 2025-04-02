from django.contrib.auth.models import User
from django.db import models

from config import PRODUCT_TYPES


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    category = models.CharField(max_length=255, choices=PRODUCT_TYPES, unique=True, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    stock = models.IntegerField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    vendor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='product_images/', default='')
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(null=False, blank=False)
    comment = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"

