from django.db import models
from getdata.models import Cleaned
from beacon.models import Beacon

Cleaned.objects.all().delete()
loopctrl=Beacon.objects.last()
for i in range(loopctrl.id,0,-1):
	obj=Beacon.objects.get(id=i)
	Cleaned.objects.create(employee_number='default',ssid=obj.beacon_name,signal_strength='-1111' )
	print(obj.beacon_name)