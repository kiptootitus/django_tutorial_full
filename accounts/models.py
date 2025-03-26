from django.db import models
from phonenumber_field.modelfields import PhoneNumberField  # If using 

class Address(models.Model):
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.zip_code}, {self.state}"

class Profile(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, blank=True, null=True)  # Changed to EmailField
    phone = PhoneNumberField(blank=True, null=True)  # If using django-phonenumber-field

    def __str__(self):
        return self.name if self.name else "Unnamed Profile"
