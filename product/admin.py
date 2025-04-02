from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

from .models import Product, ProductReview



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'vendor',  'date_created', 'date_modified')
    search_fields = ('name',)
    ordering = ['-name']
    list_filter = ('category', 'name')
    fields = ('name', 'description', 'category', 'price', 'stock', 'vendor','images')

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    extra = 1
    fields = ('user', 'rating', 'comment', 'product')
    list_display = ('product', 'user', 'rating', 'comment', 'date_created', 'date_modified')
    search_fields = ('product__name', 'user__username')
    list_filter = ('product', 'user')
    ordering = ['-date_created']

    def date_created(self, obj):
        return obj.date_created.strftime('%Y-%m-%d %H:%M:%S')

    date_created.short_description = 'Created At'




