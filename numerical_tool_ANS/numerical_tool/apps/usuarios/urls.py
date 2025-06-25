from django.urls import path
from . import views

# Estas URLs manejan el registro, inicio de sesión y cierre de sesión de usuarios.

app_name = 'usuarios'

urlpatterns = [
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('registro/', views.registro_usuario, name='registro'),
    path('historial/', views.historial_general, name='historial_general'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
]