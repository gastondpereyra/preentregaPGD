from django import forms

class ClientesFormulario(forms.Form):
	nombre = forms.CharField()
	nrocliente = forms.IntegerField()

class ProveedorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    empresa= forms.CharField(max_length=30)
    email= forms.EmailField()
    nroproveedor= forms.IntegerField(max_length=30)



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		# Saca los mensajes de ayuda
		help_texts = {k:"" for k in fields}