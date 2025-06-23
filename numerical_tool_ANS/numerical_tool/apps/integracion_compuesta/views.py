from django.shortcuts import render

def index(request):
    return render(request, 'integracion_compuesta/index.html')