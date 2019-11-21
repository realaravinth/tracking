from django.shortcuts import render
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from .models import Location
from .forms import Search_form
from .search import search_matches,process_location
from beacon.models import Beacon
from django.contrib.auth.decorators import login_required


state="default value"

@login_required
def create_search(request):
	if request.method == 'POST':
		form=Search_form(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			state=search_matches(form.cleaned_data)
			form = Search_form()
			if state=="not found":
				form=(Search_form)
				return render(request, "search.html",{'form':Search_form})
			else:
				return HttpResponseRedirect('/search-results')
	return render(request, "search.html",{'form':Search_form})


@login_required
def display_results(request):
	location=Location.objects.last()
	context		={
		"room_pretext":"Employee is at room ",
		"room_number":location.room,
		"floor_pretext":"in floor number ",
		"floor_number":location.floor
	}
	
	return render(request, "search-results.html",context)
    




	

