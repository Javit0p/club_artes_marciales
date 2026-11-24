from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.db.models import Q
from .models import Alumno
from .forms import AlumnoForm

def es_administrador(user):
    return user.groups.filter(name='Administrador').exists() or user.is_superuser

def puede_editar(user):
    return es_administrador(user) or user.groups.filter(name='Supervisor').exists()

@login_required
def dashboard_view(request):
    user = request.user
    context = {
        'es_admin': es_administrador(user),
        'es_supervisor': user.groups.filter(name='Supervisor').exists(),
        'es_administrativo': user.groups.filter(name='Administrativo').exists(),
    }
    return render(request, 'dashboard.html', context)

@login_required
def alumno_list(request):
    user = request.user
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
        'es_admin': es_administrador(user),
        'es_supervisor': user.groups.filter(name='Supervisor').exists(),
    })

@login_required
def alumno_create(request):
    if not puede_editar(request.user):
        return redirect('alumno_list')
    if request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('alumno_list')
    else:
        form = AlumnoForm()
    return render(request, 'dojoApp/alumno_form.html', {'form': form, 'titulo': 'Registrar Nuevo Alumno'})

@login_required
def alumno_update(request, pk):
    if not puede_editar(request.user):
        return redirect('alumno_list')
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('alumno_list')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'dojoApp/alumno_form.html', {'form': form, 'titulo': f'Editar Alumno: {alumno.nombre}'})

@login_required
def alumno_delete(request, pk):
    if not puede_editar(request.user):
        return redirect('alumno_list')
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('alumno_list')
    return render(request, 'dojoApp/alumno_confirm_delete.html', {'alumno': alumno})

@login_required
def gestionar_usuarios(request):
    if not es_administrador(request.user):
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ese nombre de usuario ya existe.')
        else:
            nuevo_usuario = User.objects.create_user(username=username, email=email, password=password)
            grupo_admin, _ = Group.objects.get_or_create(name='Administrador')
            nuevo_usuario.groups.add(grupo_admin)
            messages.success(request, f'Administrador {username} creado con éxito.')
        return redirect('gestionar_usuarios')

    usuarios = User.objects.all()
    for u in usuarios:
        u.es_admin = es_administrador(u)
    return render(request, 'dojoApp/gestionar_usuarios.html', {'usuarios': usuarios})

@login_required
def hacer_admin(request, user_id):
    if not es_administrador(request.user):
        return redirect('dashboard')
    usuario = get_object_or_404(User, pk=user_id)
    grupo_admin, _ = Group.objects.get_or_create(name='Administrador')
    usuario.groups.add(grupo_admin)
    messages.success(request, f'{usuario.username} ahora es Administrador.')
    return redirect('gestionar_usuarios')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')