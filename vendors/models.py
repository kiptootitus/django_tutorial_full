from django.db import models
from django.contrib.auth.models import User
from accounts_handler import AccountsHandler  # Assuming this is a valid import
from functools import wraps
from django.core.validators import MinValueValidator, MaxValueValidator

try:
    from config import PLAN_CHOICES
except ImportError:
    # Define fallback if config is missing
    PLAN_CHOICES = (
        ('Free', 'Free'),
        ('Premium', 'Premium'),
    )
def get_default_user():
    first_user = User.objects.first()
    return first_user.id if first_user else None

class Vendor(models.Model):  # Removed AccountsHandler inheritance
    description = models.TextField(max_length=50, blank=False, null=False)
    vendor_email = models.EmailField(null=False, blank=False, default='')
    seller_name = models.CharField(max_length=50, blank=False, null=False)
    store_name = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['seller_name']
        unique_together = ['description', 'vendor_email', 'seller_name', 'store_name']

    def __str__(self):
        return self.store_name

class Subscription(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    plan_type = models.CharField(max_length=20, choices=PLAN_CHOICES, default='Free')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.vendor.store_name} - {self.plan_type}"

class VendorBankDetail(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)
    swift_code = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)

    class Meta:
        unique_together = ['vendor', 'bank_name', 'account_number', 'swift_code']
    
    def __str__(self):
        return f"{self.vendor.store_name} - {self.bank_name}"

class VendorReview(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        null=True,
        blank=True,
        default=get_default_user  # Will now return an ID or None
    )
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)],validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.vendor.store_name} by {self.user.username if self.user else 'Anonymous'}"