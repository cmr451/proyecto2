from django.db import models

# Create your models here.

class Cliente(models.Model):
	id_cliente = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 30) 
	apellidos = models.CharField(max_length = 30)
	edad = models.IntegerField()
	email = models.EmailField()
	def __str__(self):
		return self.nombre+' '+self.apellidos

class Producto(models.Model):
	id_producto = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 30)
	tamaño = models.CharField(max_length = 30)
	precio = models.IntegerField()
	imagen = models.ImageField(upload_to = 'img')

	def __str__(self):
		return self.nombre+' '+self.tamaño
