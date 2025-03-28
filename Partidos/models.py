from django.db import models
from Deportes.models import Campeonato

class Partido(models.Model):
    ESTADOS = (('programado', 'Programado'), ('en_curso', 'En Curso'), ('finalizado', 'Finalizado'))
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    fecha_partido = models.DateTimeField()
    marcador = models.CharField(max_length=20, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='programado')
