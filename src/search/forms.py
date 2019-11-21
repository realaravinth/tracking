from django import forms


class Search_form(forms.Form):
	employee_number  	= forms.CharField()
	