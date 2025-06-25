# apps/integracion_compuesta/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import HistorialIntegracion
from .utils import trapecio_compuesto_detallado_educativo, generar_grafica
import time
import matplotlib
matplotlib.use('Agg')  # Esto evita los errores de hilos y Tkinter
import matplotlib.pyplot as plt
import io
import base64

def index(request):
    if request.method == 'POST':
        funcion = request.POST.get('funcion', '').strip()
        a_str = request.POST.get('a', '')
        b_str = request.POST.get('b', '')
        n_str = request.POST.get('n', '')

        # Validaciones explícitas antes del try
        if not funcion:
            return render(request, 'integracion_compuesta/index.html', {
                'error': 'Debes ingresar una función.',
                'funcion': funcion, 'a': a_str, 'b': b_str, 'n': n_str
            })
        try:
            a = float(a_str)
            b = float(b_str)
            n = int(n_str)
        except ValueError:
            return render(request, 'integracion_compuesta/index.html', {
                'error': 'Los valores de a, b y n deben ser numéricos.',
                'funcion': funcion, 'a': a_str, 'b': b_str, 'n': n_str
            })

        if n <= 0:
            return render(request, 'integracion_compuesta/index.html', {
                'error': 'El número de subintervalos (n) debe ser mayor que 0.',
                'funcion': funcion, 'a': a, 'b': b, 'n': n
            })
        if a >= b:
            return render(request, 'integracion_compuesta/index.html', {
                'error': 'El límite inferior (a) debe ser menor que el superior (b).',
                'funcion': funcion, 'a': a, 'b': b, 'n': n
            })

        try:
            time.sleep(1.2)
            resultado_detallado, error = trapecio_compuesto_detallado_educativo(funcion, a, b, n)
            if error or not resultado_detallado:
                return render(request, 'integracion_compuesta/index.html', {
                    'error': error[0] if error else 'Error al evaluar la función.',
                    'funcion': funcion, 'a': a, 'b': b, 'n': n
                })

            # --- Generar la gráfica y convertirla a base64 ---
            fig = generar_grafica(funcion, a, b, n)

            if not hasattr(fig, "savefig"):
                return render(request, 'integracion_compuesta/index.html', {
                    'error': 'No se pudo generar la gráfica. Verifica la función ingresada.',
                    'funcion': funcion, 'a': a, 'b': b, 'n': n
                })
            
            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            plt.close(fig)
            buf.seek(0)
            grafica = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()
            plt.close(fig)
            # -------------------------------------------------

            if request.user.is_authenticated:

                # Guardar el historial de integración
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
            
            else:
                return redirect('usuarios:login')

        except Exception as e:
            return render(request, 'integracion_compuesta/index.html', {
                'error': f'Ocurrió un error inesperado: {str(e)}',
                'funcion': funcion, 'a': a, 'b': b, 'n': n
            })

    return render(request, 'integracion_compuesta/index.html')

@login_required
def resultado(request):
    resultado = request.session.get('resultado')
    secciones = request.session.get('secciones')
    grafica = request.session.get('grafica')

    # Limpia la sesión si lo deseas
    request.session.pop('resultado', None)
    request.session.pop('secciones', None)
    request.session.pop('grafica', None)
    
    if resultado is None:
        return redirect('integracion_compuesta:integracion_home')
    return render(request, 'integracion_compuesta/result.html', {
        'resultado': resultado,
        'secciones': secciones,
        'grafica': grafica
    })

def historial(request):   
    return redirect('usuarios:historial_general')
