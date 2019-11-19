from django.shortcuts import render
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from .models import Search, Results, Location
from .forms import Search_form
from .search import search_matches,process_location
from beacon.models import Beacon
from django.contrib.auth.decorators import login_required
from getdata.delete_values import delete_all




state="default value"
@login_required
def create_search(request):
	# Results.objects.all().delete()
	# delete_all()
	if request.method == 'POST':
		form=Search_form(request.POST)
		if form.is_valid():
			# Search.objects.create(**form.cleaned_data)
			print(form.cleaned_data)
			state=search_matches(form.cleaned_data)
			form = Search_form()
			
			if state=="not found":
				form=(Search_form)
				return render(request, "search.html",{'form':Search_form})
			else:
				# process_location(state)
				return HttpResponseRedirect('/search-results')
	return render(request, "search.html",{'form':Search_form})
@login_required
def display_results(request):
	print(state)
	location=Location.objects.last()
	print(location)
	context		={
		"room_pretext":"Employee is at room ",
		"room_number":location.room,
		"floor_pretext":"in floor number ",
		"floor_number":location.floor
	}
	print(context)
	
	return render(request, "search-results.html",context)
    




	

