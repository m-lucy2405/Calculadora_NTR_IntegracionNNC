from django.shortcuts import render, redirect
from .forms import NewtonRaphsonForm
from .utils import newton_raphson_method
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import HistorialNewtonRaphson as NRHistorial

# Vista para manejar el formulario de Newton-Raphson y mostrar resultados

def index(request):
    form = NewtonRaphsonForm()
    return render(request, 'newton_raphson/index.html', {'form': form})

@login_required
def resolver(request):
    if request.method == 'POST':
        form = NewtonRaphsonForm(request.POST)
        if form.is_valid():
            funcion = form.cleaned_data['funcion']
            x0 = form.cleaned_data['valor_inicial']
            tol = form.cleaned_data['tolerancia']
            iter_max = form.cleaned_data['iteraciones']

            resultados, raiz, error, total_iters, convergio = newton_raphson_method(funcion, x0, tol, iter_max)

            # Guardar historial
            NRHistorial.objects.create(
                usuario=request.user,
                funcion=funcion,
                valor_inicial=x0,
                tolerancia=tol,
                iteraciones_maximas=iter_max,
                raiz_aproximada=raiz,
                error_final=error,
                total_iteraciones=total_iters,
                exito=convergio
            )

            return render(request, 'newton_raphson/result.html', {
                'resultados': resultados,
                'convergio': convergio,
                'funcion': funcion
            })
    else:
        form = NewtonRaphsonForm()

    return render(request, 'newton_raphson/index.html', {'form': form})

@login_required
def historial(request):
    historial_integracion = NRHistorial.objects.filter(usuario=request.user).order_by('-fecha')
    historial_newton = NRHistorial.objects.filter(usuario=request.user).order_by('-fecha')
    
    return render(request, 'usuarios/historial_general.html', {
        'historial_integracion': historial_integracion,
        'historial_newton': historial_newton,
    })
