# apps/integracion_compuesta/models.py

from django.db import models
from django.contrib.auth.models import User

class HistorialIntegracion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='historial_integracion')
    funcion = models.CharField(max_length=255)
    a = models.FloatField()
    b = models.FloatField()
    n = models.IntegerField()
    resultado = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.funcion} - {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}"