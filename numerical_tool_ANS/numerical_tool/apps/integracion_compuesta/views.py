from django.shortcuts import render, redirect
from .forms import IntegracionForm
from .utils import integrar_compuesto_trapecio
from .models import IntegracionResultado

def index(request):
    if request.method == 'POST':
        form = IntegracionForm(request.POST)
        if form.is_valid():
            funcion = form.cleaned_data['funcion']
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            n = form.cleaned_data['n']

            resultado, pasos = integrar_compuesto_trapecio(funcion, a, b, n)

            IntegracionResultado.objects.create(
                funcion=funcion,
                a=a,
                b=b,
                n=n,
                resultado=resultado
            )

            context = {
                'funcion': funcion,
                'a': a,
                'b': b,
                'n': n,
                'resultado': resultado,
                'pasos': pasos
            }
            return render(request, 'integracion_compuesta/result.html', context)
    else:
        form = IntegracionForm()

    return render(request, 'integracion_compuesta/index.html', {'form': form})

def historial(request):
    resultados = IntegracionResultado.objects.all().order_by('-fecha')
    return render(request, 'integracion_compuesta/historial.html', {'resultados': resultados})
