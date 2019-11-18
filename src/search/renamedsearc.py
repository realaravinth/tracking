from django.db import models
from .models import Search,Results
from signal_sort.models import Signal_sort
from signal_sort.signal_sort import signal_sort
from tracker_registration.models import Tracker_register
from django.http import HttpResponse
from django.shortcuts import render

def Search_matches():
	signal_sort()
	search_term			=Search.objects.last()
	search_term_object	=Search.objects.get(id=search_term.id)
	num_employee		=Tracker_register.objects.latest('id')
	num 				=num_employee.id
	for x in range(num,0,-1):
		emp_id=Tracker_register.objects.get(id=x)
		if search_term_object.employee_num!=emp_id.tracker_number:
			print( "not found" )
			return("404")
		else:
			sorted_rec_latest 			=Signal_sort.objects.latest('id')
			sorted_rec_latest_object	=Signal_sort.objects.get(id=sorted_rec_latest.id)
			num 						=sorted_rec_latest_object.id
			for x in range(num,0,-1):
				obj = Signal_sort.objects.get(id=num)
				if search_term_object.employee_num==obj.employee_num :
					Results.objects.create(employee_num=obj.employee_num,bssid=obj.bssid,signal_strength=obj.signal_strength)
					print("suckess")
					return("sucess")
					break







	#    else:
	# 	sorted_rec_latest 			=Signal_sort.objects.latest('id')
	#         sorted_rec_latest_object	=Signal_sort.objects.get(id=sorted_rec_latest.id)
	#         num 						=sorted_rec_latest_object.id
	#         for x in range(num,0,-1):
	#     		obj = Signal_sort.objects.get(id=num)
	#     		if search_term_object.employee_num==obj.employee_num :
	#     		Results.objects.create(employee_num=obj.employee_num,bssid=obj.bssid,signal_strength=obj.signal_strength)
	#     		Search.objects.all().delete()
	# # return "found"	
					





