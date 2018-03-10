from django.db import models

# Create your models here.
class Kotrana001_Model001(models.Model):
    name = models.CharField(
        max_length = 120
    )

    def __str__(self):
        return self.name 


class Kotrana001_Model002(models.Model):
	first_name = models.CharField(
		max_length = 120
	)
	last_name = models.CharField(
		max_length = 120
	)

	def __str__(self):
		return self.first_name + ' '+ self.last_name