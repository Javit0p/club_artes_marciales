from django.urls import path
from . import views

urlpatterns = [
    path('', views.alumno_list, name='alumno_list'),
    path('nuevo/', views.alumno_create, name='alumno_create'),
    path('editar/<int:pk>/', views.alumno_update, name='alumno_update'),
    path('eliminar/<int:pk>/', views.alumno_delete, name='alumno_delete'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
]