from django.db import models
from dojoApp.models import Alumno

class Evento(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título del Evento")
    fecha = models.DateField(verbose_name="Fecha del Evento")
    lugar = models.CharField(max_length=150, verbose_name="Lugar / Sede")
    descripcion = models.TextField(verbose_name="Descripción")

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.titulo


class InscripcionEvento(models.Model):
    ESTADO_PAGO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Pagado', 'Pagado'),
    ]

    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='inscripciones', verbose_name="Alumno")
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscripciones', verbose_name="Evento")
    fecha_inscripcion = models.DateField(auto_now_add=True, verbose_name="Fecha de Inscripción")
    estado_pago = models.CharField(max_length=15, choices=ESTADO_PAGO_CHOICES, default='Pendiente', verbose_name="Estado de Pago")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")

    class Meta:
        verbose_name = "Inscripción a Evento"
        verbose_name_plural = "Inscripciones a Eventos"
        unique_together = ('alumno', 'evento')

    def __str__(self):
        return f"{self.alumno.nombre} - {self.evento.titulo}"