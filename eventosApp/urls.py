from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
]