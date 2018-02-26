from django.db import models

# Create your models here.
class RRestaurants(models.Model):
    name = models.CharField(
        max_length = 120
    )

    def __str__(self):
        return self.name


class RRestaurantsLocation(models.Model):
    name = models.CharField(
        max_length = 120
    )
    location = models.CharField(
        max_length = 120
    )
    category = models.CharField(
        max_length = 120, 
        # null = True,   # mbola tsy haiko we fa maninn reto ligne ak2 reto no tsy mety
        # blank = True 
    )
    timestamp = models.DateTimeField(auto_now_add = True )  # to know the first added of this object
    updated = models.DateTimeField(     # when you did an update, you are going to save that time of the update
        auto_now = True
    )
    date_field001 = models.DateTimeField(
        auto_now = True
        , auto_now_add = False
    )

    def __str__(self):
        return self.name