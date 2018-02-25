from django.contrib import admin

# Register your models here.
from .models import RRestaurants, RRestaurantsLocation
 # from .models import RestaurantLocation

admin.site.register(RRestaurants)
admin.site.register(RRestaurantsLocation)