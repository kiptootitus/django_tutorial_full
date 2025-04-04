from django.db import models
from rest_framework.reverse import reverse
from rest_framework import serializers
from .models import Product, ProductReview, ProductCategory
from config import PRODUCT_TYPES
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Adjust fields as needed


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
    reviews = ProductReviewSerializer(many=True, required=False)
    vendor_user = serializers.PrimaryKeyRelatedField(read_only=True)  # Return only the ID
    url = serializers.HyperlinkedIdentityField(view_name='product_detail', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'url': {'read_only': True},
        }


    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError(_("Product name cannot be empty."))
        return value

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product_detail", kwargs={"pk": obj.pk}, request=request)
    
    def validate_category(self, value):
        valid_categories = [choice[0] for choice in PRODUCT_TYPES]
        if value not in valid_categories:
            raise serializers.ValidationError(_("Invalid product type."))
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
    # def validate(self, attrs):
    #     if attrs['category'] not in PRODUCT_TYPES:
    #         raise serializers.ValidationError(_("Invalid product type."))
    #     return attrs
    def create(self, validated_data):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            validated_data["vendor"] = request.user
        return super().create(validated_data)
    def update(self, instance, validated_data):
        # Handle nested reviews data
        reviews_data = validated_data.pop('reviews', [])
        
        # Update product fields
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.price = validated_data.get('price', instance.price)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.images = validated_data.get('images', instance.images)  # Handle images correctly
        instance.vendor= validated_data.get('vendor', instance.vendor)
        instance.save()

        # Update or create reviews
        for review_data in reviews_data:
            review_id = review_data.get('id', None)
            if review_id:
                # Update existing review
                review = ProductReview.objects.get(id=review_id, product=instance)
                for attr, value in review_data.items():
                    setattr(review, attr, value)
                review.save()
            else:
                # Create new review
                ProductReview.objects.create(product=instance, **review_data)

        return instance
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['reviews'] = ProductReviewSerializer(instance.reviews.all(), many=True).data
        return representation



