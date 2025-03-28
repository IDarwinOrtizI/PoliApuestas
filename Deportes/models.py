# deportes/models.py
from django.db import models

class Deporte(models.Model):
    nombre = models.CharField(max_length=100)


class Campeonato(models.Model):
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()