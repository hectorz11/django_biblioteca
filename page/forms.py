from django import forms
from .models import *

class addLibroForm(forms.ModelForm):
	class Meta:
		model = Libro

class addPeriodicoForm(forms.ModelForm):
	class Meta:
		model = Periodico