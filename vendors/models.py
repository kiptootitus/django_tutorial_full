from django.db import models
from django.contrib.auth.models import User
from accounts_handler import AccountsHandler
from functools import wraps

from config import PLAN_CHOICES
# Create your models here.

class Vendor(models.Model, AccountsHandler):  # Swap the order
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255, blank=False, null=False)
    vendor_email = models.EmailField()
    seller_name = models.CharField(max_length=255, blank=False, null=False)
    store_name = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['seller_name']

    def __str__(self):
        return self.store_name


class Subscription(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    plan_type = models.CharField(max_length=20, choices=PLAN_CHOICES, default="free")
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.vendor.store_name} - {self.plan_type}"


class VendorBankDetail(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=50)  # For India, can change to SWIFT/BIC for international
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.vendor.store_name} - {self.bank_name}"


class VendorReview(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.vendor.store_name} by {self.user.username}"
