from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request): #request contiene información de la petición web al servidor Django
    return HttpResponse('Hi body') #response HttpResponse manda información en el navegador

def despedida(request):
    return HttpResponse('Bye man')

def contacto(request):
    return HttpResponse('Contacto: Conmigo, email: mimail@mail.com')
