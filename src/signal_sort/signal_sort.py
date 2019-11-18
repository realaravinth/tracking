from django.db import models
from sort.models import Sorted
from .models import Signal_sort

def signal_sort():
	last=Sorted.objects.last()
	first=Sorted.objects.first()
	lastObj=Sorted.objects.get(id=last.id)
	firstObj=Sorted.objects.get(id=first.id)
	# num=last.id-first.id
	loopCtrl=1
	for i in range (last.id,first.id,-loopCtrl):
		loopCtrl=1
		obj=Sorted.objects.get(id=i)
		empid=obj.employee_num
		obj2=Sorted.objects.get(id=i-1)
		if empid==obj2.employee_num:
			loopCtrl+=1
			stronger=obj.signal_strength
			strongerBSSID=obj.bssid
			if obj.signal_strength>obj2.signal_strength:
				stronger=obj.signal_strength
				strongerBSSID=obj.bssid

			else:
				greater=obj2.signal_strength
				strongerBSSID=obj2.bssid
			for x in range(i-2,first.id,-1):
				objX=Sorted.objects.get(id=x-1)
				if greater<objX.signal_strength:
					greater=objX.signal_strength
					strongerBSSID=objX.bssid

				loopCtrl+=1

			Signal_sort.objects.create(employee_num=empid,
									bssid=strongerBSSID,
									signal_strength=greater	
									)
	# Sorted.objects.all().delete()





			
				





