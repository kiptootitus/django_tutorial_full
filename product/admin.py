from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

from .models import Product, ProductCategory, ProductImage, ProductReview


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return '-'

    image_preview.short_description = 'Image Preview'

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    extra = 1
    fields = ('user', 'rating', 'comment')
    ordering = ['-date_created']

    def date_created(self, obj):
        return obj.date_created.strftime('%Y-%m-%d %H:%M:%S')

    date_created.short_description = 'Created At'

class ProductCategoryInline(admin.TabularInline):
    model = ProductCategory
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ['-name']
    list_filter = ('name',)
    fields = ( 'name', 'description')

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')
    search_fields = ('name',)
    ordering = ['-name']
    list_filter = ('category', 'name')
    inlines = [ProductImageInline, ProductCategoryInline]
    fields = ('name', 'description', 'category', 'price', 'stock')

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser



