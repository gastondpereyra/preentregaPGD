from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(Clientes)

admin.site.register(Proveedores)

admin.site.register(Vendedores)

admin.site.register(Entregas)
