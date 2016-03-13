from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from address.models import AddressField



# Create your models here.

class FoodType(models.Model):
	type = models.CharField(max_length=50)


class Restaurant(models.Model):
	name = models.CharField()
	description = models.TextField()
	type = models.ManyToManyField(FoodType)
	location = AddressField()
	createdOn = models.DateField(blank=True)
    createdBy = models.CharField(max_length=30)
    logo = models.ImageField(upload_to=uploadPath, default='default.png', editable=True)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    isActive = models.BooleanField(default=True)




class FoodItem(models.model):
	restaurant_name = models.ForiegnKey(Restaurant)
	item_name = models.CharField(max_length=50)
	type = models.ManyToManyField(FoodType)
	description = models.TextField()
	price = models.CharField(max_length=10)
	createdOn = models.DateField(blank=True)
    createdBy = models.CharField(max_length=30)
    logo = models.ImageField(upload_to=uploadPath, default='default.png', editable=True)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    isActive = models.BooleanField(default=True)



class Review(models.model):
	restaurant_name = models.ForiegnKey(Restaurant)
	food_name = models.ForiegnKey(FoodType)
	comment = models.TextField()
	user = models.ForiegnKey(User)



