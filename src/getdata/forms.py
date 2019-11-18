from django import forms

from .models import Scan

class Dumpdataform(forms.Form):
	employee_num  	= forms.CharField()
	bssid   			= forms.CharField()
	signal_strength			=forms.IntegerField()