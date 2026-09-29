from django.shortcuts import render
from .models import Evento

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventosApp/evento_list.html', {'eventos': eventos})

def sobre_nosotros(request):
    return render(request, 'eventosApp/sobre_nosotros.html')