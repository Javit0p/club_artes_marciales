from django.db import models

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