# apps/integracion_compuesta/urls.py

from django.urls import path
from . import views

app_name = 'integracion_compuesta'

urlpatterns = [
    path('', views.index, name='integracion_home'),
    path('resultado/', views.resultado, name='resultado'),
    path('historial/', views.historial, name='historial'),
]