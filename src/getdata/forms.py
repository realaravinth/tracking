from django import forms

from .models import Scan

class Dumpdataform(forms.Form):
	employee_number  	= forms.CharField()
	ssid   			= forms.CharField()
	signal_strength			=forms.IntegerField()