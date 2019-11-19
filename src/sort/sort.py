from django.db import models
from django.contrib.auth.models import User
from getdata.models import Scan
from beacon.models import Beacon
from .models import Sorted
from signal_sort.signal_sort import signal_sort

def sort_data(dump):
	# latest_scan=Scan.objects.last()
	# latest_scan_object=Scan.objects.get(id=latest_scan.id)
	num_beacon	=Beacon.objects.latest('id')
	num=num_beacon.id
	for x in range (num,0,-1):
		registered_beacon=Beacon.objects.get(id=x)
		if dump['bssid']==registered_beacon.beacon_name:
			# Sorted.objects.create(employee_num=dump['employee_num'],
			# 						bssid=dump['bssid'],
			# 						signal_strength=dump['signal_strength']
			# 					)
			# a=Sorted.objects.last()
			
			Sorted.objects.get(bssid=dump['bssid']).delete()

			Sorted.objects.create(employee_num=dump['employee_num'],
									bssid=dump['bssid'],
									signal_strength=dump['signal_strength'])

			# signal_sort(dumnp)
								

