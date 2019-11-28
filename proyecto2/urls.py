"""proyecto2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tienda import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('contacto/', views.contacto,name='contacto'),
   
    path('registro_cli/', views.registro_cli, name= 'registro_cli'),
    path('galeria_edit/', views.mostrar_pro, name= 'mostrar_pro'),
    path('editar_pro/<int:id>', views.editar_pro, name= 'editar_pro'),
    path('eliminar_pro/<int:id>', views.eliminar_pro, name= 'eliminar_pro'),
    
    path('registro_pro/', views.registro_pro, name='registro_pro'),
    path('cliente_edit/', views.mostrar_cli, name= 'mostrar_cli'),
    path('editar_cli/<int:id>', views.editar_cli, name= 'editar_cli'),
    path('eliminar_cli/<int:id>', views.eliminar_cli, name= 'eliminar_cli'),

    path('index2/', views.index2, name='index2'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)