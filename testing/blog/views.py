from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from .models import Blog
from .forms import Testform


# def displaydump(request,*args,**kwargs):
# 	latest=Scan.objects.latest('id')
# 	print(latest)
# 	latest_entry=Scan.objects.get(id=latest.id)
# 	context={	'empid':latest_entry.employee_num,
# 				'bssid':latest_entry.bssid,
# 				'strength':latest_entry.signal_strength,
# 	}

# 	return render(request,"arduinodumpform.html",context)

def create_dump(request):
	my_form = Testform()
	if request.method == "POST":
		my_form = Testform(request.GET)
		my_form = Testform()
		print(my_form)
		if my_form.is_valid():
			Blog.objects.create(**my_form.cleaned_data)
			print(my_form.cleaned_data)
			my_form = Testform()


	context		={
		"form": my_form,
	}

	return render(request,"form.html",context)