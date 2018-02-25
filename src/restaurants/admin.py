from django.contrib import admin

# Register your models here.
from .models import Restaurant
 # from .models import RestaurantLocation

admin.site.register(Restaurant)
# admin.site.register(RestaurantLocation)