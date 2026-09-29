from django.contrib import admin
from .models import CategoriaCinturon, Alumno

@admin.register(CategoriaCinturon)
class CategoriaCinturonAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'documento', 'cinturon', 'horario', 'estado', 'fecha_ingreso')
    list_filter = ('estado', 'cinturon')
    search_fields = ('nombre', 'documento')