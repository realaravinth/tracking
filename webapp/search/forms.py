from django import forms

from .models import Search

class Search_form(forms.Form):
	employee_num  	= forms.CharField()
	