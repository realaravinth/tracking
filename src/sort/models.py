
from django.db import models

class Sorted(models.Model):
	employee_num	=models.CharField(max_length=20,default='admin',)
	bssid				=models.CharField(max_length=30)
	signal_strength		=models.IntegerField()
	class Meta:
		verbose_name_plural = "Sorted Data"
	
		  