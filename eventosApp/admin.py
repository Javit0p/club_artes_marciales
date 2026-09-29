from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'lugar')
    search_fields = ('titulo', 'lugar')
    list_filter = ('fecha',)