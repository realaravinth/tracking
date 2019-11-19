from django.db import models
from sort.models import Sorted
from .models import Signal_sort

# def signal_sort():
# 	# Signal_sort.objects.all().delete()
# 	last=Sorted.objects.last()
# 	first=Sorted.objects.first()
	
# 	# num=last.id-first.id
# 	loopCtrl=1
# 	for i in range (last.id,first.id,-loopCtrl):
# 		loopCtrl=1
# 		obj=Sorted.objects.get(id=i)
# 		empid=obj.employee_num
# 		obj2=Sorted.objects.get(id=i-1)
# 		if empid==obj2.employee_num:
# 			loopCtrl+=1
# 			greater=obj.signal_strength
# 			strongerBSSID=obj.bssid
# 			if obj.signal_strength>obj2.signal_strength:
# 				greater=obj.signal_strength
# 				strongerBSSID=obj.bssid

# 			else:
# 				greater=obj2.signal_strength
# 				strongerBSSID=obj2.bssid
# 			for x in range(i-2,first.id,-1):
# 				objX=Sorted.objects.get(id=x-1)
# 				if greater<objX.signal_strength:
# 					greater=objX.signal_strength
# 					strongerBSSID=objX.bssid

# 				loopCtrl+=1
			
# 			Signal_sort.objects.create(employee_num=empid,
# 									bssid=strongerBSSID,
# 									signal_strength=greater	
# 									)
# 	# Sorted.objects.all().delete()
def signal_sort(search):
	count=0
	ids="0 "
	possible=Sorted.objects.filter(employee_num=search)
	for a in possible:
		count+=1
		ids+=str(a.id)+' '
	ids=ids.split()
	stronger=Sorted.objects.last()
	for i in range (count,0,-2):
		a=Sorted.objects.get(id=ids[i])
		b=Sorted.objects.get(id=ids[i-1])
		stronger=b
		if a.signal_strength>b.signal_strength:
			stronger=a
	# Signal_sort.objects.create(employee_num=stronger.employee_num,
	# 								bssid=stronger.bssid,
	# 								signal_strength=stronger.signal_strength
	# 								)
	return stronger.bssid
	

		




			
				





