from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from .models import Scan
from .forms import Dumpdataform
from sort.sort import sort_data
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



@csrf_exempt
def create_dump(request):
	my_form=Dumpdataform()
	my_form=Dumpdataform(request.POST)
	if my_form.is_valid():
		Scan.objects.create(**my_form.cleaned_data)	
		a=sort_data()
		Scan.objects.all().delete()
		# my_form=Dumpdataform()
	context={
			"form":my_form,
	}

	return render(request, "arduinodumpform.html", context)

# def displaydump(request,*args,**kwargs):
# 	latest=Scan.objects.latest('id')
# 	print(latest)
# 	latest_entry=Scan.objects.get(id=latest.id)
# 	context={	'empid':latest_entry.employee_num,
# 				'bssid':latest_entry.bssid,
# 				'strength':latest_entry.signal_strength,
# 	}

# 	return render(request,"arduinodumpform.html",context)

# def create_dump(request):
# 	my_form = Dumpdataform()
# 	# if request.method == "POST":
# 	my_form = Dumpdataform(request.GET)
# 	if my_form.is_valid():
# 	    my_form = Dumpdataform()
# 		# if my_form.is_valid():
# 		# 	 Scan.objects.create(**my_form.cleaned_data)
# 		# 	 print(my_form.cleaned_data)
# 		#      my_form = Dumpdataform()
# 	 	Scan.objects.create({employee_num:employee_num,bssid:bissd,signal_strength:signal_strength}.**my_form)			
# 	   #Scan.objects.create(**my_form.cleaned_data)
# 	     # my_form = Dumpdataform()


# 	context		={
# 		"form": my_form,
# 	}

# 	return render(request,"arduinodumpform.html",context)
#  below one was working alright until I fucked it up
# def create_dump(request):
# 	my_form=Dumpdataform()
# 	my_form=Dumpdataform(request.GET)
# 	if my_form.is_valid():
# 		# Scan.objects.create({
# 			# #employee_num:enum,
# 			# bssid:bissd,
# 			# signal_strength:signal_strength},
# 			# **my_form)
# 		Scan.objects.create({employee_num:employee_num,bssid:bissd,signal_strength:signal_strength},**my_form)
# 		my_form=Dumpdataform()
# 	context= {
# 		"form":my_form,
# 	}
# 	return render(request, "arduinodumpform.html", context)