from django.shortcuts import render
from django.shortcuts import redirect
from .models import Producto
from .models import Cliente
from .forms import *

# Create your views here.



def registro_pro(request):
	if request.method == 'POST':
		form2 = ProductoForm(request.POST, request.FILES)
		if form2.is_valid():
			form2.save()
			return redirect('mostrar_pro')
	else:
		form2 = ProductoForm()
		return render(request, 'registro_pro.html',{'form2':form2})

def mostrar_pro(request):
	producto =Producto.objects.all() 
	contexto = {'productos':producto}
	return render(request, 'galeria_edit.html', contexto)

def editar_pro(request, id):
	producto = Producto.objects.get(id_producto=id)
	if request.method == 'GET':
		form = ProductoForm(instance=producto)
	else:
		form = ProductoForm(request.POST, instance=producto)
		if form.is_valid():
			form.save()
			return redirect('mostrar_pro')
	return render(request, 'registro_pro.html',{'form2':form}) 

def eliminar_pro(request, id):
	producto = Producto.objects.get(id_producto=id)
	if request.method == 'POST':
		producto.delete()
		return redirect('mostrar_pro')
	return render(request, 'eliminar_pro.html', {'producto':producto})


def registro_cli(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else: 
		form = ClienteForm()
		return render(request, 'registro_cli.html',{'form':form})
def mostrar_cli(request):
	cliente = Cliente.objects.all()
	contexto2 = {'clientes':cliente}
	return render(request, 'cliente_edit.html', contexto2)

def editar_cli(request, id):
	cliente = Cliente.objects.get(id_cliente=id)
	if request.method == 'GET':
		form = ClienteForm(instance= cliente)
	else:
		form = ClienteForm(request.POST, instance= cliente)
		if form.is_valid():
			form.save()
			return redirect('mostrar_cli')
	return render(request, 'registro_cli.html', {'form':form})

def eliminar_cli(request, id):
	cliente = Cliente.objects.get(id_cliente=id)
	if request.method == 'POST':
		cliente.delete()
		return redirect('mostrar_cli')
	return render(request, 'eliminar_cli.html', {'cliente':cliente})

	
def index(request):
	return render(request,'index.html')

def index2(request):
	return render(request,'index2.html')

def galeria(request):
	producto = Producto.objects.all() 
	contexto = {'productos':producto}
	return render(request,'galeria.html', contexto)

def contacto(request):
	return render(request,'contacto.html')