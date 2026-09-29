from django.urls import path
from . import views

app_name = 'dojo'

urlpatterns = [
    path('', views.lista_alumnos, name='lista_alumnos'),
    path('alumno/<int:alumno_id>/', views.detalle_alumno, name='detalle_alumno'),
    path('alumno/crear/', views.crear_alumno, name='crear_alumno'),
    path('alumno/modificar/<int:alumno_id>/', views.modificar_alumno, name='modificar_alumno'),
    path('alumno/eliminar/<int:alumno_id>/', views.eliminar_alumno, name='eliminar_alumno'),
]