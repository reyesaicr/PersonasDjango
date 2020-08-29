"""sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from webapp.views import bienvenido, despedida, contacto  # Primero hay que definir el método en el views y marcar la carpeta contenedora de la app principal como Mark as/Sources Root usando click derecho

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('bienvenido/', bienvenido)
    path('', bienvenido),
    path('despedida.html', despedida), #Soporta con y sin extensiones
    path('contacto', contacto)
]
