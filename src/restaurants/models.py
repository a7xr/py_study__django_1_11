from django.db import models
from django.utils import timezone
# Create your models here.



class RestaurantLocation(models.Model):
    name = models.CharField(
        max_length = 120
    )
    location = models.CharField(
        max_length = 120
    )
    category = models.CharField(
        max_length = 120, 
        null = True,   
        blank = True  
    )
    timestamp = models.DateTimeField(auto_now_add = True )  # to know the first added of this object
    updated = models.DateTimeField(     # when you did an update, you are going to save that time of the update
        auto_now = True
    )
    date_field001 = models.DateTimeField(
        auto_now = False
        , auto_now_add = False
    )

class Restaurant(models.Model):
    name = models.CharField(
        max_length = 120
    )
