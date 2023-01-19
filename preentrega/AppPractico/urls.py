from django.urls import path

from AppPractico import views


urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('clientes', views.clientes, name="Clientes"),
    path('proveedores', views.proveedores, name="Proveedores"),
    path('vendedores', views.vendedores, name="Vendedores"),
    path('entregas', views.entregas, name="Entregas"),
    path('clientesFormulario', views.clientesFormulario, name="ClientesFormulario"),
    path('busquedanrocliente', views.nrocliente, name="BusquedaClientes"),
    path('buscar/', views.buscar)
]
