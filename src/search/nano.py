from django.db import models
from .models import Search,Results
from signal_sort.models import Signal_sort
from signal_sort.signal_sort import signal_sort
from tracker_registration.models import Tracker_register
from django.http import HttpResponse
from django.shortcuts import render

def search_matches():
    signal_sort()
    search_term	=Search.objects.last()
    search_term_object=Search.objects.get(id=search_term.id)
    num_employee=Tracker_register.objects.latest('id')
    num=num_employee.id
    status="not found"
    for x in range(num,0,-1):
        emp_id=Tracker_register.objects.get(id=x)
        sorted_rec_latest                       =Signal_sort.objects.latest('id')
        sorted_rec_latest_object=Signal_sort.objects.get(id=sorted_rec_latest.id)
        num                                             =sorted_rec_latest_object.id
        for x in range(num,0,-1):
		obj =Signal_sort.objects.get(id=num)
		if search_term_object.employee_num==obj.employee_num:
		print(obj.employee_num,obj.bssid,obj.signal_strength)
		Results.objects.create(employee_num=obj.employee_num,bssid=obj.bssid,signal_strength=obj.signal_strength)
		status="found"
		print("sess")
		break
	return status
