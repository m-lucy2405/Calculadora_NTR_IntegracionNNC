from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def documentacion_integracion(request):
    return render(request, 'core/documentacion_integracion.html')

def documentacion_newton(request):
    return render(request, 'core/documentacion_newton.html')