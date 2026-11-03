from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Evento, InscripcionEvento
from .forms import EventoForm, InscripcionForm

@login_required
def evento_list(request):
    query = request.GET.get('q', '')
    if query:
        eventos = Evento.objects.filter(titulo__icontains=query)
    else:
        eventos = Evento.objects.all()
    return render(request, 'eventosApp/evento_list.html', {'eventos': eventos, 'query': query})

@login_required
def evento_create(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    else:
        form = EventoForm()
    return render(request, 'eventosApp/evento_form.html', {'form': form, 'titulo': 'Crear Nuevo Evento'})

@login_required
def evento_update(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventosApp/evento_form.html', {'form': form, 'titulo': f'Editar Evento: {evento.titulo}'})

@login_required
def evento_delete(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('evento_list')
    return render(request, 'eventosApp/evento_confirm_delete.html', {'evento': evento})

# --- VISTAS DE TRANSACCIÓN ---

@login_required
def inscripcion_list(request):
    inscripciones = InscripcionEvento.objects.select_related('alumno', 'evento').all()
    return render(request, 'eventosApp/inscripcion_list.html', {'inscripciones': inscripciones})

@login_required
def inscripcion_create(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscripcion_list')
    else:
        form = InscripcionForm()
    return render(request, 'eventosApp/inscripcion_form.html', {'form': form})