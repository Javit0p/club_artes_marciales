from django.db import models

class CategoriaCinturon(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Cinturón / Grado")
    
    class Meta:
        verbose_name = "Categoría de Cinturón"
        verbose_name_plural = "Categorías de Cinturones"

    def __str__(self):
        return self.nombre


class Alumno(models.Model):
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]

    nombre = models.CharField(max_length=100, verbose_name="Nombre Completo")
    documento = models.CharField(max_length=20, unique=True, verbose_name="Documento / RUT")
    horario = models.CharField(max_length=100, verbose_name="Horario de Entrenamiento")
    cinturon = models.ForeignKey(CategoriaCinturon, on_delete=models.CASCADE, related_name='alumnos', verbose_name="Cinturón")
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='Activo', verbose_name="Estado")
    fecha_ingreso = models.DateField(auto_now_add=True, verbose_name="Fecha de Ingreso")

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return f"{self.nombre} ({self.documento})"