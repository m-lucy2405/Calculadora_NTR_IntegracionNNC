from django.urls import path
from . import views

# Estas URLs manejan el registro, inicio de sesión y cierre de sesión de usuarios.

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
]