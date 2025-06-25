from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    nombre_completo = models.CharField(max_length=150, blank=True, default="N/A")
    carrera = models.CharField(max_length=100, blank=True, default="N/A")
    carnet = models.CharField(max_length=20, blank=True, default="N/A")
    ciclo = models.CharField(max_length=10, blank=True, default="N/A")
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'