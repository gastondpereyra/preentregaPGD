from django.db import models

# Create your models here.
class Clientes(models.Model):

    nombre=models.CharField(max_length=40)
    nrocliente=models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - camada: {self.nrocliente}"


class Proveedores(models.Model):
    nombre= models.CharField(max_length=30)
    empresa= models.CharField(max_length=30)
    email= models.EmailField()
    nroproveedor = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - empresa: {self.empresa} - email: {self.email}- Proveedor nro: {self.nroproveedor}"

class Vendedores(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

class Entregas(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    entrega = models.BooleanField()
