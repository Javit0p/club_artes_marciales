from django import forms
from .models import Evento, InscripcionEvento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'fecha', 'lugar', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Torneo Nacional ITF 2026'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lugar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Gimnasio Central'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Detalles del evento...'}),
        }

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = InscripcionEvento
        fields = ['alumno', 'evento', 'estado_pago', 'observaciones']
        widgets = {
            'alumno': forms.Select(attrs={'class': 'form-select'}),
            'evento': forms.Select(attrs={'class': 'form-select'}),
            'estado_pago': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Ej. Categoría Juvenil / Pago abonado'}),
        }