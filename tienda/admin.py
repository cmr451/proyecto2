from django.contrib import admin
from .models import Cliente
from .models import Producto

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	pass
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	pass
