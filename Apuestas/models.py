from django.db import models
from Partidos.models import Partido
from Cuentas.models import CustomUser

class Apuesta(models.Model):
    ESTADOS = (('activa', 'Activa'), ('ganada', 'Ganada'), ('perdida', 'Perdida'))
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    monto_apuesta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_apuesta = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='activa')
