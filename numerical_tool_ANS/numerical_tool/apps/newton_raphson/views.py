from django.shortcuts import render, redirect
from .forms import NewtonRaphsonForm
from .utils import newton_raphson_method
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import NRHistorial

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
            iters = form.cleaned_data['iteraciones']

            resultados, convergio = newton_raphson_method(funcion, x0, tol, iters)

            # Guardar historial
            NRHistorial.objects.create(
                usuario=request.user,
                funcion=funcion,
                valor_inicial=x0,
                tolerancia=tol,
                iteraciones_usadas=len(resultados),
                convergio=convergio,
                fecha=now()
            )

            return render(request, 'newton_raphson/result.html', {
                'resultados': resultados,
                'convergio': convergio,
                'funcion': funcion
            })
    else:
        form = NewtonRaphsonForm()

    return render(request, 'newton_raphson/index.html', {'form': form})
