from django import forms

class ClientesFormulario(forms.Form):
	nombre = forms.CharField()
	nrocliente = forms.IntegerField()