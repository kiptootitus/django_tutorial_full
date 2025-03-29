from django.contrib import admin
from .models import Vendor, Subscription, VendorBankDetail, VendorReview

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'seller_name', 'vendor_email', 'is_active', 'created_at', 'modified_at')
    search_fields = ('store_name', 'seller_name', 'vendor_email')
    list_filter = ('is_active', 'created_at')
    ordering = ('seller_name',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'plan_type', 'start_date', 'end_date', 'is_active')
    search_fields = ('vendor__store_name', 'plan_type')
    list_filter = ('plan_type', 'is_active', 'start_date')
    raw_id_fields = ('vendor',)

@admin.register(VendorBankDetail)
class VendorBankDetailAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'bank_name', 'account_number', 'is_verified')
    search_fields = ('vendor__store_name', 'bank_name', 'account_number')
    list_filter = ('is_verified',)
    raw_id_fields = ('vendor',)

@admin.register(VendorReview)
class VendorReviewAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'user', 'rating', 'created_at')
    search_fields = ('vendor__store_name', 'user__username', 'review')
    list_filter = ('rating', 'created_at')
    raw_id_fields = ('vendor', 'user')