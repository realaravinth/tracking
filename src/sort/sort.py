from django.db import models
from django.contrib.auth.models import User
from getdata.models import Scan
from beacon.models import Beacon
from .models import Sorted


def sort_data():
	latest_scan=Scan.objects.last()
	latest_scan_object=Scan.objects.get(id=latest_scan.id)
	num_beacon	=Beacon.objects.latest('id')
	num=num_beacon.id
	for x in range (num,0,-1):
		registered_beacon=Beacon.objects.get(id=x)
		if latest_scan_object.bssid==registered_beacon.beacon_name:
			Sorted.objects.create(employee_num=latest_scan_object.employee_num,
									bssid=latest_scan_object.bssid,
									signal_strength=latest_scan_object.signal_strength
								)

