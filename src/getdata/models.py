		  
from django.db import models

class Cleaned(models.Model):
	employee_number	=models.CharField(max_length=20)
	ssid				=models.CharField(max_length=30)
	signal_strength		=models.IntegerField()
	class Meta:
		verbose_name_plural = "Cleaned Data"
	