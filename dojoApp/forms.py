from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'documento', 'horario', 'cinturon', 'estado', 'foto', 'documentos']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Javier Pérez'}),
            'documento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 1234567-5'}),
            'horario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Horario infantil'}),
            'cinturon': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'documentos': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }