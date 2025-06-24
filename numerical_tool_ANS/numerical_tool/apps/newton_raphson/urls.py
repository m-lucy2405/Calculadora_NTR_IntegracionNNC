from django.urls import path
from . import views

# URLs para la aplicación de Newton-Raphson y proteccion por autenticación

app_name = 'newton_raphson'

urlpatterns = [
    path('', views.index, name='newton_home'),
    path('resolver/', views.resolver, name='resolver'),
    path('historial/', views.historial, name='historial'),
]
