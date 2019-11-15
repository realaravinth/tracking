from django import forms

from .models import Blog

class Testform(forms.Form):
	testing_field  	= forms.CharField()
