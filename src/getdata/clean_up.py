from django.db import models
from django.contrib.auth.models import User
from .models import Scan, Cleaned
from beacon.models import Beacon



def clean(dump):
	num_beacon	=Beacon.objects.latest('id')
	num=num_beacon.id
	for x in range (num,0,-1):
		registered_beacon=Beacon.objects.get(id=x)
		if dump['ssid']==registered_beacon.beacon_name:
			Cleaned.objects.get(ssid=dump['ssid']).delete()
			Cleaned.objects.create(employee_number=dump['employee_number'],
									ssid=dump['ssid'],
									signal_strength=dump['signal_strength'])

			
								

