		  
from django.db import models

# Create your models here.
class Scan(models.Model):
	employee_number	=models.CharField(max_length=20)
	ssid				=models.CharField(max_length=30)
	signal_strength		=models.IntegerField()
	class Meta:
		verbose_name_plural = "Datadump from trackers"
	
class Cleaned(models.Model):
	employee_number	=models.CharField(max_length=20)
	ssid				=models.CharField(max_length=30)
	signal_strength		=models.IntegerField()
	class Meta:
		verbose_name_plural = "Cleaned Data"
	