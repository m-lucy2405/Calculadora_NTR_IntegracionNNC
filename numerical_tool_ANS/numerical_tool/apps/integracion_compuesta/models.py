from django.db import models

class IntegracionResultado(models.Model):
    funcion = models.CharField(max_length=100)
    a = models.FloatField()
    b = models.FloatField()
    n = models.IntegerField()
    resultado = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"∫ {self.funcion} de {self.a} a {self.b} = {self.resultado}"
