from django.db import models


class Beacon(models.Model):
	beacon_name	=models.CharField(max_length=100) 
	room		=models.IntegerField()
	floor		=models.IntegerField()
	