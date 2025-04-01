from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField  # If using

from config import ROLE_CHOICES


class Address(models.Model):
    street = models.CharField(max_length=25, blank=False, null=False, default='')
    city = models.CharField(max_length=25, blank=False, null=False, default='')
    zip_code = models.CharField(max_length=25, blank=False, null=False, default='')
    state = models.CharField(max_length=25, blank=False, null=False, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['state']
        unique_together = ('street', 'city', 'state', 'zip_code')

    def __str__(self):
        return f"{self.street}, {self.city}, {self.zip_code}, {self.state}"


class Profile(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False, default='')
    last_name = models.CharField(max_length=50, blank=False, null=False, default='')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, blank=False, null=False, unique=True, default='email')
    phone = PhoneNumberField(blank=False, null=False, unique=True, default='phone')

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.email}, {self.phone}"


class Flights(models.Model):
    airline = models.CharField(max_length=255, blank=False, null=False)
    flight = models.CharField(max_length=255, blank=False, null=False)
    source_city = models.CharField(max_length=255, blank=False, null=False)
    departure_time = models.CharField(max_length=255, blank=False, null=False)
    stops = models.CharField(max_length=255, blank=False, null=False)
    arrival_time = models.CharField(max_length=255, blank=False, null=False)
    destination_city = models.CharField(max_length=255, blank=False, null=False)
    duration = models.FloatField(max_length=255, blank=False, null=False)
    days_left = models.IntegerField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.airline}, {self.source_city}, {self.destination_city}, {self.price}"

    @property
    def get_airline(self):
        return self.airline


class AccountManager(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CUSTOMER')
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.role} - {self.address}"
