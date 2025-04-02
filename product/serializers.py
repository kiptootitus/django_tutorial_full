from django.db import models
from rest_framework import serializers
from .models import Product, ProductImage, ProductReview, ProductCategory
from config import PRODUCT_TYPES
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage



class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError(_("Category name cannot be empty."))
        return value
    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError(_("Category description cannot be empty."))
        return value
    def create(self, validated_data):
        category = ProductCategory.objects.create(**validated_data)
        return category
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'read_only': True},
        }
    def validate_image(self, value):
        if not value:
            raise serializers.ValidationError(_("Image cannot be empty."))
        return value
    def create(self, validated_data):
        image = ProductImage.objects.create(**validated_data)
        return image
    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'read_only': True},
        }
    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(_("Rating must be between 1 and 5."))
        return value
    def validate_comment(self, value):
        if not value:
            raise serializers.ValidationError(_("Comment cannot be empty."))
        return value
    def create(self, validated_data):
        review = ProductReview.objects.create(**validated_data)
        return review
    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)
    reviews = ProductReviewSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError(_("Product name cannot be empty."))
        return value

    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError(_("Product description cannot be empty."))
        return value
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(_("Price must be a positive number."))
        return value
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError(_("Stock cannot be negative."))
        return value
    def validate_category(self, value):
        if not value:
            raise serializers.ValidationError(_("Category cannot be empty."))
        return value
    def validate_vendor(self, value):
        if not value:
            raise serializers.ValidationError(_("Vendor cannot be empty."))
        return value
    def validate(self, attrs):
        if attrs['category'] not in PRODUCT_TYPES:
            raise serializers.ValidationError(_("Invalid product type."))
        return attrs
    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        reviews_data = validated_data.pop('reviews', [])
        product = Product.objects.create(**validated_data)
        for image_data in images_data:
            ProductImage.objects.create(product=product, **image_data)
        for review_data in reviews_data:
            ProductReview.objects.create(product=product, **review_data)
        return product
    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', [])
        reviews_data = validated_data.pop('reviews', [])
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.price = validated_data.get('price', instance.price)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.vendor = validated_data.get('vendor', instance.vendor)
        instance.save()
        for image_data in images_data:
            ProductImage.objects.create(product=instance, **image_data)
        for review_data in reviews_data:
            ProductReview.objects.create(product=instance, **review_data)
        return instance
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerializer(instance.images.all(), many=True).data
        representation['reviews'] = ProductReviewSerializer(instance.reviews.all(), many=True).data
        return representation



