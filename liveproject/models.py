from django.db import models

# Create your models here.
class register_tb(models.Model):
	UserName = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)


class prodcuct_tb(models.Model):
	product_name = models.CharField(max_length = 255)
	category = models.CharField(max_length = 255)
	image = models.ImageField(upload_to="media/")
	discription = models.CharField(max_length = 300)
	

class condact_tb(models.Model):
	Name=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	Number=models.CharField(max_length=255)
	Message=models.CharField(max_length=255)

class image_enter_tb(models.Model):
	images = models.ImageField(upload_to="media/")