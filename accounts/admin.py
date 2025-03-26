from django.contrib import admin
from .models import Address, Profile
# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'zip_code', 'date_created', 'date_modified')
    search_fields = ('street', 'city', 'state', 'zip_code')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ("name", "address", "email", "phone")
  search_fields = ("name", "email")