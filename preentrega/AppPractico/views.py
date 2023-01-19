from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppPractico.models import Clientes

# Create your views here.

def Clientes(request):

      clientes =  Clientes(nombre="Juan Perez", nrocliente="0001")
      clientes.save()
      documentoDeTexto = f"--->Curso: {clientes.nombre}   Numero de cliente : {cliente.nrocliente}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppPractico/inicio.html")

def clientes(request):

      return render(request, "AppPractico/clientes.html")

def proveedores(request):

      return render(request, "AppPractico/proveedores.html")


def vendedores(request):

      return render(request, "AppPractico/vendedores.html")


def entregas(request):

      return render(request, "AppPractico/entregas.html")

from AppPractico.forms import ClientesFormulario

def clientesFormulario(request):
	if request.method == "POST":
		miFormulario = ClientesFormulario(request.POST) # Aqui me llega la informacion del html
		print(miFormulario)
		if miFormulario.is_valid:
			informacion = miFormulario.cleaned_data
			cliente = Clientes(nombre=informacion["clientes"], nrocliente=informacion["nrocliente"])
			cliente.save()		
			return render(request, "AppPractico/inicio.html")
	else:
		miFormulario = ClientesFormulario()
	return render(request, "AppPractico/ClientesFormulario.html", {"miFormulario": miFormulario})


def nrocliente(request):
	return render(request, "AppPractico/busquedanrocliente.html")



def buscar(request):
	respuesta = f"Estoy buscando el cliente nro: {request.GET['nrocliente']}"
	#No olvidar from django.http import HttpResponse
	return HttpResponse(respuesta)