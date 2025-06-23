from django.db import models
from django.contrib.auth.models import User

# Modelo para guardar el historial de ejecuciones del método de Newton-Raphson
# Este modelo almacena el usuario, la función, el valor inicial, la tolerancia, 
# el número de iteraciones utilizadas, si convergió o no, y la fecha de ejecución.

class NRHistorial(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    funcion = models.CharField(max_length=200)
    valor_inicial = models.FloatField()
    tolerancia = models.FloatField()
    iteraciones_usadas = models.IntegerField()
    convergio = models.BooleanField()
    fecha = models.DateTimeField()
    
    def __str__(self):
        return f"{self.usuario.username} - {self.funcion} - {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}"
