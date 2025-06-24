from django.urls import path
from . import views

app_name = 'newton_raphson'

urlpatterns = [
    path('', views.home, name='newton_home'),
]