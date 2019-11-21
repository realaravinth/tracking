from django import forms



class Dumpdataform(forms.Form):
	employee_number  	= forms.CharField()
	ssid   			= forms.CharField()
	signal_strength			=forms.IntegerField()