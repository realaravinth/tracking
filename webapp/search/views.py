from django.shortcuts import render
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from .models import Search, Results
from .forms import Search_form
from .search import Search_matches
from beacon.models import Beacon

def create_search(request):
	if request.method == 'POST':
		form=Search_form(request.POST)
		if form.is_valid():
			Search.objects.create(**form.cleaned_data)
			print(form.cleaned_data)
			form = Search_form()
			state=Search_matches()
			if state=="found":
				# display_results(request)
				results=display_results(request)
			return HttpResponseRedirect('/search-results')
	else:
		form=Search_form()
	return render(request, "search.html", {'form':Search_form})	

def display_results(request):
	location=process_location()

	# if location.bssid[2]==1:
	context		={
		"room_pretext":"Employee is at room ",
		"room_number":location.room,
		"floor_pretext":"in floor number: ",
		"floor_number":location.floor
	}

	return render(request, "search-results.html",context)
    
    


def process_location(): #might have to pass results into function
	result_term			=Results.objects.last()
	result_object		=Results.objects.get(id=result_term.id)
	# num_employee		=Tracker_register.get.latest('id')
	beacon 				= result_object.bssid
	beacon_id			=Beacon.objects.latest('id')
	beacon_num 			=beacon_id.id
	for x in range(beacon_num,0,-1):
		obj=Beacon.objects.get(id=x)
		if obj.beacon_name==result_object.bssid:
			return obj



## 	my_form = Search_form()
# 	if request.method == "POST":
# 		my_form = Search_form(request.POST)
# 		# my_form = Search_form()
# 		if my_form.is_valid():
# 			Search.objects.create(**my_form.cleaned_data)
# 			print(my_form.cleaned_data)
# 			my_form = Search_form()
# 			state=Search_matches()
# 			if state=="found":
# 				# display_results(request)
# 				results=display_results(request)
# 				return HttpResponseRedirect('/search-results') 	

# 				# location=process_location()
# 				# if location.bssid[2]==1:
				
# 				# return render(request, "search.html",context)
# 			# else:
# 			# 	return render(request, "not_found.html",{})
#    #  		else:
#    #  			context		={
# 			# 		"form": my_form,
# 			# # "room_pretext":"Employee is at room ",
# 			# # "room_number":location.room,
# 			# # "floor_pretext":"in floor number: ",
# 			# # "floor_number":location.floor
# 			# 			}
# 			# 	return render(request, "search.html",context)			   	

# 	# context		={
# 	# 	"form": my_form,
# 	# 	# "room_pretext":"Employee is at room ",
# 	# 	# "room_number":location.room,
# 	# 	# "floor_pretext":"in floor number: ",
# 	# 	# "floor_number":location.floor
# 	# }
	

# 	# return render(request,"search.html",context)

# state=Search_matches()
# if state=="found":



	
