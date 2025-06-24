# apps/integracion_compuesta/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import HistorialIntegracion
from .utils import evaluar_funcion, trapecio_compuesto_detallado_educativo, generar_grafica
import time

def index(request):
    if request.method == 'POST':
        funcion = request.POST.get('funcion', '').strip()
        try:
            a = float(request.POST.get('a', ''))
            b = float(request.POST.get('b', ''))
            n = int(request.POST.get('n', ''))

            if n <= 0 or a >= b:
                raise ValueError("Intervalo o n inválido")

            time.sleep(1.2)
            resultado_detallado, error = trapecio_compuesto_detallado_educativo(funcion, a, b, n)
            if error or not resultado_detallado:
                return render(request, 'integracion_compuesta/index.html', {
                    'error': error[0] if error else 'Error al evaluar la función.',
                    'funcion': funcion, 'a': a, 'b': b, 'n': n
                })

            grafica = generar_grafica(funcion, a, b, n)
            HistorialIntegracion.objects.create(
                usuario=request.user,
                funcion=funcion,
                a=a,
                b=b,
                n=n,
                resultado=resultado_detallado['resultado']
            )

            return render(request, 'integracion_compuesta/result.html', {
                'resultado': resultado_detallado['resultado'],
                'secciones': resultado_detallado['secciones'],
                'grafica': grafica
            })

        except Exception as e:
            return render(request, 'integracion_compuesta/index.html', {
                'error': 'Error al procesar los datos. Verifica tus entradas.',
                'funcion': funcion, 'a': request.POST.get('a', ''), 'b': request.POST.get('b', ''), 'n': request.POST.get('n', '')
            })

    return render(request, 'integracion_compuesta/index.html')

def resultado(request):
    return redirect('integracion_compuesta:integracion_home')

@login_required
def historial(request):
    historial = HistorialIntegracion.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'integracion_compuesta/historial.html', {'historial': historial})