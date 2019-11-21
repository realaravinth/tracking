from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from .forms import Dumpdataform
from .clean_up import clean
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
 

@csrf_exempt
def create_dump(request):
	
	my_form=Dumpdataform()
	my_form=Dumpdataform(request.GET)
	if my_form.is_valid():
		clean(my_form.cleaned_data)
		my_form=Dumpdataform()
	context={
			"form":my_form,
	}
	

	return render(request, "getdata.html", context)


