from django import forms 
from .models import *

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		exclude =['id_producto']


class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		exclude =['id_cliente']

