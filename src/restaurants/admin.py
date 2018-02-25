from django.contrib import admin

# Register your models here.
from .models import Restaurant, RestaurantLocation

admin.site.register(Restaurant)
admin.site.register(RestaurantLocation)