from django.urls import path

from AppPractico import views

from django.contrib.auth.views import LogoutView


urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('clientes', views.clientes, name="Clientes"),
    path('proveedores', views.proveedores, name="Proveedores"),
    path('vendedores', views.vendedores, name="Vendedores"),
    path('entregas', views.entregas, name="Entregas"),
    path('clientesFormulario', views.clientesFormulario, name="ClientesFormulario"),
    path('busquedanrocliente', views.nrocliente, name="BusquedaClientes"),
    path('buscar/', views.buscar),
    path("leerProveedores", views.leerProveedores, name = "LeerProveedores"),
    path('eliminarProveedor/<Proveedores_nombre>/', views.eliminarProveedor, name="EliminarProveedor"),
    path('editarProveedor/<Proveedores_nombre>/', views.editarProveedor, name="EditarProveedor"),
    path('clientes/list', views.ClienteList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ClienteDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ClienteCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ClienteUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ClienteDelete.as_view(), name='Delete'),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppPractico/logout.html'), name='Logout'),
]
