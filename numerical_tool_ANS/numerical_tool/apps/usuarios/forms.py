from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Formulario para el registro de usuarios personalizado.
# Este formulario hereda de UserCreationForm y añade campos adicionales como email,
# nombre completo, carrera, carnet, ciclo y foto.
# El campo 'foto' es opcional y permite a los usuarios subir una imagen de perfil

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nombre_completo = forms.CharField(max_length=150)
    carrera = forms.CharField(max_length=100)
    carnet = forms.CharField(max_length=20)
    ciclo = forms.CharField(max_length=10)
    foto = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'nombre_completo', 'email', 'password1', 'password2', 'carrera', 'carnet', 'foto']
