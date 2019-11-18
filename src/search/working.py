from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from .models import Search, Results
from .forms import Search_form
from .search import Search_matches
from beacon.models import Beacon

def process_location(): #might have to pass results into function
	result_term			=Results.objects.last()
	result_object		=Results.objects.get(id=result_term.id)
	# num_employee		=Tracker_register.get.latest('id')
	beacon 				= result_object.bssid
	beacon_id			=Beacon.objects.latest('id')
	beacon_num 			=beacon_id.id
	# for x in range(beacon_num,0,-1):
	# 	obj=Beacon.objects.get(id=x)
	# 	if obj.beacon_name==result_object.bssid:
	# 		# return obj
	# 		print(obj)
