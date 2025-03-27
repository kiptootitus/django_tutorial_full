from django.contrib import admin
from .models import Address, Flights, Profile
# Register your models here.
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'zip_code', 'date_created', 'date_modified')
    search_fields = ('street', 'city', 'state', 'zip_code')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ("name", "address", "email", "phone")
  search_fields = ("name", "email")
  
  

@admin.register(Flights)
class FlightsAdmin(admin.ModelAdmin):
  list_display = ( "airline", "flight", "source_city", "departure_time", "stops", 
        "arrival_time", "destination_city", "duration", "days_left", "price")
  search_fields = ("airline", "flight")
  