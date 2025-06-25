from django.db import models
from django.contrib.auth.models import User

# Modelo para guardar el historial de ejecuciones del método de Newton-Raphson
# Este modelo almacena el usuario, la función, el valor inicial, la tolerancia, 
# el número de iteraciones utilizadas, si convergió o no, y la fecha de ejecución.

class HistorialNewtonRaphson(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='historial_newton')
    funcion = models.CharField(max_length=255)
    valor_inicial = models.FloatField()
    tolerancia = models.FloatField()
    iteraciones_maximas = models.IntegerField()
    raiz_aproximada = models.FloatField(null=True, blank=True)
    error_final = models.FloatField(null=True, blank=True)
    total_iteraciones = models.IntegerField()
    exito = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario.username} - {self.funcion} - {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}"
