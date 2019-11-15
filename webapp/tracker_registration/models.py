from django.db import models


class Tracker_register(models.Model):
	tracker_number	=models.CharField(max_length=20) 
	class Meta:
		verbose_name_plural = "Register"
		# app_label = 'Trackers'
