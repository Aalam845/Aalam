from django.db import models

# Create your models here.

class car(models.Model):
	name_car = models.CharField(max_length=25)
	date_car = models.DateField()

	def __str__(self):
		return self.name_car

class house(models.Model):
	name_house = models.CharField(max_length=25)
	date_house = models.DateField()

	def __str__(self):
		return self.name_house
