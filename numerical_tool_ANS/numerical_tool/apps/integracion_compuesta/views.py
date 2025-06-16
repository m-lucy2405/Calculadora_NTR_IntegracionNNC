from django.shortcuts import render

def home(request):
    return render(request, 'integracion_compuesta/home.html')