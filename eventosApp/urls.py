from django.urls import path
from . import views

urlpatterns = [
    path('', views.evento_list, name='evento_list'),
    path('nuevo/', views.evento_create, name='evento_create'),
    path('editar/<int:pk>/', views.evento_update, name='evento_update'),
    path('eliminar/<int:pk>/', views.evento_delete, name='evento_delete'),
    
    # Rutas de Transacción
    path('inscripciones/', views.inscripcion_list, name='inscripcion_list'),
    path('inscripciones/nueva/', views.inscripcion_create, name='inscripcion_create'),
]