from django.urls import path
from . import views

app_name = 'integracion_compuesta'

urlpatterns = [
    path('', views.index, name='index'),
    path('historial/', views.historial, name='historial'),
]
