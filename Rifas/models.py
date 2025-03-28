# rifas/models.py
from django.db import models
from Cuentas.models import CustomUser

class Rifa(models.Model):
    ESTADOS = (('activa', 'Activa'), ('cerrada', 'Cerrada'), ('sorteada', 'Sorteada'))
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    max_participantes = models.IntegerField()
    valor_boleteria = models.DecimalField(max_digits=10, decimal_places=2)
    premio_principal = models.TextField()
    premios_secundarios = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='activa')

class Boleteria(models.Model):
    ESTADOS = (('activa', 'Activa'), ('ganadora', 'Ganadora'), ('no_ganadora', 'No Ganadora'))
    rifa = models.ForeignKey(Rifa, on_delete=models.CASCADE)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    numero_boleto = models.CharField(max_length=50, unique=True)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='activa')

