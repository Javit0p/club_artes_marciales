from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Alumno
from .forms import AlumnoForm

@login_required
def dashboard_view(request):
    user = request.user
    es_admin = user.groups.filter(name='Administrador').exists() or user.is_superuser
    es_supervisor = user.groups.filter(name='Supervisor').exists()
    es_administrativo = user.groups.filter(name='Administrativo').exists()

    context = {
        'es_admin': es_admin,
        'es_supervisor': es_supervisor,
        'es_administrativo': es_administrativo,
    }
    return render(request, 'dashboard.html', context)

@login_required
def alumno_list(request):
    user = request.user
    es_admin = user.groups.filter(name='Administrador').exists() or user.is_superuser
    es_supervisor = user.groups.filter(name='Supervisor').exists()

    query = request.GET.get('q', '')
    if query:
        alumnos = Alumno.objects.filter(
            Q(nombre__icontains=query) | Q(documento__icontains=query)
        )
    else:
        alumnos = Alumno.objects.all()
    
    return render(request, 'dojoApp/alumno_list.html', {
        'alumnos': alumnos, 
        'query': query,
        'es_admin': es_admin,
        'es_supervisor': es_supervisor,
    })

@login_required
def alumno_create(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumno_list')
    else:
        form = AlumnoForm()
    return render(request, 'dojoApp/alumno_form.html', {'form': form, 'titulo': 'Registrar Nuevo Alumno'})

@login_required
def alumno_update(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('alumno_list')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'dojoApp/alumno_form.html', {'form': form, 'titulo': f'Editar Alumno: {alumno.nombre}'})

@login_required
def alumno_delete(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('alumno_list')
    return render(request, 'dojoApp/alumno_confirm_delete.html', {'alumno': alumno})

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')