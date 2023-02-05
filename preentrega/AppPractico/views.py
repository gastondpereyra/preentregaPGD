from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppPractico.models import Clientes, Proveedores
from AppPractico.forms import ClientesFormulario, ProveedorFormulario

# Create your views here.

def clientes(request):

      clientes =  Clientes(nombre="Juan Perez", nrocliente="0001")
      clientes.save()
      documentoDeTexto = f"--->Curso: {clientes.nombre}   Numero de cliente : {clientes.nrocliente}"


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
			cliente = Clientes(nombre=informacion["nombre"], nrocliente=informacion["nrocliente"])
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



def leerProveedores(request):
	Proveedores = proveedores.objects.all() #trae todos los proveedores
	contexto= {"Proveedores":Proveedores}
	return render(request, "AppPractico/leerProveedores.html",contexto)

def eliminarProveedor(request, Proveedores_nombre):

	proveedor = proveedores.objects.get(nombre=Proveedores_nombre)
	proveedor.delete()
	# vuelvo al menú
	proveedores = proveedores.objects.all() # trae todos los profesores
	contexto = {"proveedores": proveedores}
	return render(request, "AppPractico/leerProveedores.html", contexto)

def editarProveedor(request, Proveedores_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    proveedor = proveedores.objects.get(nombre=Proveedores_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = ProveedorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            proveedor.nombre = informacion['nombre']
            proveedor.empresa = informacion['empresa']
            proveedor.email = informacion['email']
            proveedor.nroproveedor = informacion['nroproveedor']

            proveedor.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppPractico/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = ProveedorFormulario(initial={'nombre': proveedor.nombre, 'empresa': proveedor.empresa,
                                                   'email': proveedor.email, 'nro de cliente': proveedor.nroproveedor})

    # Voy al html que me permite editar
    return render(request, "AppPractico/editarProveedor.html", {"miFormulario": miFormulario, "proveedor_nombre": Proveedores_nombre})

from django.views.generic import ListView

class ClienteList(ListView):
      model = Clientes
      template_name = "AppCoder/clientes_list.html"

from django.views.generic.detail import DetailView

class ClienteDetalle(DetailView):
      model = Clientes
      template_name = "AppCoder/clientes_detalle.html"

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class ClienteCreacion(CreateView):
	model = Clientes
	success_url = "/AppPractico/clientes/list"
	fields = ['nombre', 'nrocliente']

from django.views.generic.edit import UpdateView

class ClienteUpdate(UpdateView):
	model = Clientes
	success_url = "/AppPractico/clientes/list"
	fields = ['nombre', 'nrocliente']


from django.views.generic.edit import DeleteView


class ClienteDelete(DeleteView):
      model = Clientes
      success_url = "/AppCoder/clientes/list"


#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data = request.POST)
		if form.is_valid(): # Si pasó la validación de Django
			usuario = form.cleaned_data.get('username')
			contrasenia = form.cleaned_data.get('password')

			user = authenticate(username= usuario, password=contrasenia)
			if user is not None:
				login(request, user)
				return render(request, "AppPractico/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
			else:
				return render(request, "AppPractico/inicio.html", {"mensaje":"Datos incorrectos"})
		else:
			return render(request, "AppPractico/inicio.html", {"mensaje":"Formulario erroneo"})
	form = AuthenticationForm()
	return render(request, "AppPractico/login.html", {"form": form})


from AppPractico.forms import ClientesFormulario, ClientesFormulario, UserRegisterForm

def register(request):
	if request.method == 'POST':
		#form = UserCreationForm(request.POST)
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			form.save()
			return render(request,"AppPractico/inicio.html" , {"mensaje":"Usuario Creado :)"})
	else:
		#form = UserCreationForm()
		form = UserRegisterForm()
	return render(request,"AppPractico/registro.html" , {"form":form})

from django.contrib.auth.decorators import login_required

@login_required
def inicio(request):

	return render(request, "AppPractico/inicio.html")


@login_required
def entregas(request):

   return render(request, "AppPractico/entregas.html")