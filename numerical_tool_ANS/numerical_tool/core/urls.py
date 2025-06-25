from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('documentacion-integracion/', views.documentacion_integracion, name='documentacion_integracion'),
    path('documentacion-newton/', views.documentacion_newton, name='documentacion_newton'),
]