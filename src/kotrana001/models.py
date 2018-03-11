from django.db import models

from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator

# Create your models here.
class Kotrana001_Model001(models.Model):
    name = models.CharField(
        max_length = 120
    )

    def __str__(self):
        return self.name 

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



class Kotrana001_Model002(models.Model):
	first_name = models.CharField(
		max_length = 120
	)
	last_name = models.CharField(
		max_length = 120
	)
	slug = models.SlugField(
		null = True
		, blank = True
	)


	def __str__(self):
		return self.first_name + ' '+ self.last_name

pre_save.connect(
	rl_pre_save_receiver
	, sender=Kotrana001_Model002
)