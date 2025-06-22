from django.urls import path
from . import views

app_name = 'integracion_compuesta'

urlpatterns = [
    path('', views.integracion_view, name='vista_integracion'),
]
