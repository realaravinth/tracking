from django.db import models


class Beacon(models.Model):
	beacon_name	=models.CharField(max_length=100) 
	room		=models.IntegerField(default=None)
	floor		=models.IntegerField(default=None)
	beacon_order=models.IntegerField(default=None)