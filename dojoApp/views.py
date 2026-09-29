from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'dojoApp/alumno_list.html', {'alumnos': alumnos})

def detalle_alumno(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)
    return render(request, 'dojoApp/alumno_detail.html', {'alumno': alumno})

def crear_alumno(request):
    return redirect('dojo:lista_alumnos')

def modificar_alumno(request, alumno_id):
    return redirect('dojo:lista_alumnos')

def eliminar_alumno(request, alumno_id):
    return redirect('dojo:lista_alumnos')