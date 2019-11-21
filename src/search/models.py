from django.db import models

# Create your models here.
class Location(models.Model):
	
	room=models.IntegerField()
	floor=models.IntegerField()