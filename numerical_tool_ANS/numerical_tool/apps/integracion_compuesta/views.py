import time
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

from django.shortcuts import render

def evaluar_funcion(funcion_str, x):
    try:
        funciones_permitidas = {
            'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
            'exp': np.exp, 'log': np.log, 'sqrt': np.sqrt,
            'abs': np.abs, 'pi': np.pi, 'e': np.e,
        }
        return eval(funcion_str, {"__builtins__": {}}, {**funciones_permitidas, 'x': x})
    except Exception:
        return None

def trapecio_compuesto_detallado_educativo(funcion_str, a, b, n):
    h = (b - a) / n
    xi_vals = [a + i * h for i in range(n + 1)]
    fx_vals = []
    errores = []

    for xi in xi_vals:
        fx = evaluar_funcion(funcion_str, xi)
        if fx is None:
            errores.append(f"No se pudo evaluar la función en x = {xi}")
        fx_vals.append(fx)

    if errores:
        return None, errores

    seccion_h = {
        'titulo': '1. Cálculo del tamaño de subintervalo \\(h\\)',
        'explicacion': 'Se necesita conocer cuánto mide cada subintervalo para dividir el intervalo \\([a, b]\\). Esto se calcula como:',
        'formula': f"h = \\frac{{b - a}}{{n}} = \\frac{{{b} - {a}}}{{{n}}} = {h}"
    }

    pasos_xi = [f"$$x_{{{i}}} = {a} + {i} \\cdot {h} = {xi_vals[i]}$$" for i in range(len(xi_vals))]
    seccion_xi = {
        'titulo': '2. Cálculo de los puntos \\(x_i\\) del intervalo',
        'explicacion': 'Se generan los puntos \\(x_i\\) para evaluar la función \\(f(x)\\) en cada uno:',
        'pasos': pasos_xi
    }

    pasos_fx = [f"$$f(x_{{{i}}}) = f({xi_vals[i]}) = {fx_vals[i]}$$" for i in range(len(fx_vals))]
    seccion_fx = {
        'titulo': '3. Evaluación de la función en los puntos',
        'explicacion': 'Se evalúa la función en cada punto \\(x_i\\) para obtener los valores necesarios para la suma:',
        'pasos': pasos_fx
    }

    pasos_suma = [f"$$f(x_0) + f(x_n) = {fx_vals[0]} + {fx_vals[-1]} = {fx_vals[0] + fx_vals[-1]}$$"]
    suma = fx_vals[0] + fx_vals[-1]
    for i in range(1, n):
        parcial = 2 * fx_vals[i]
        pasos_suma.append(f"$$2 \\cdot f(x_{{{i}}}) = 2 \\cdot {fx_vals[i]} = {parcial}$$")
        suma += parcial
    resultado = (h / 2) * suma
    pasos_suma.append(f"$$\\frac{{{h}}}{{2}} \\cdot {suma} = {resultado}$$")
    seccion_suma = {
        'titulo': '4. Cálculo de la suma ponderada',
        'explicacion': 'Se aplica la fórmula del trapecio compuesto:',
        'formula': "\\frac{h}{2}\\left[f(x_0) + 2\\sum_{i=1}^{n-1} f(x_i) + f(x_n)\\right]",
        'pasos': pasos_suma
    }

    seccion_precision = {
        'titulo': '5. Notas sobre precisión y sugerencias',
        'explicacion': (
            "La precisión del método depende de cuántos subintervalos uses. "
            "A mayor \\(n\\), mejor será la aproximación. "
            "Si la función \\(f(x)\\) varía mucho en el intervalo \\([a, b]\\), podrías considerar usar la regla de Simpson para mayor precisión."
        )
    }

    return {
        'h': h,
        'xi_vals': xi_vals,
        'fx_vals': fx_vals,
        'resultado': resultado,
        'secciones': [seccion_h, seccion_xi, seccion_fx, seccion_suma, seccion_precision]
    }, None

def generar_grafica(funcion_str, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, 1000)
    y = [evaluar_funcion(funcion_str, xi) for xi in x]

    xi_vals = [a + i * h for i in range(n + 1)]
    yi_vals = [evaluar_funcion(funcion_str, xi) for xi in xi_vals]

    if any(v is None for v in y + yi_vals):
        return None

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y, label="f(x)", color="blue")
    ax.set_title("Visualización gráfica del método del trapecio compuesto")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.grid(True)

    for i in range(n):
        xs = [xi_vals[i], xi_vals[i], xi_vals[i + 1], xi_vals[i + 1]]
        ys = [0, yi_vals[i], yi_vals[i + 1], 0]
        ax.fill(xs, ys, color='skyblue', alpha=0.4)

    for i, xi in enumerate(xi_vals):
        ax.axvline(x=xi, color='gray', linestyle='--', alpha=0.3)
        ax.text(xi, -0.05 * max(yi_vals), f"$x_{{{i}}}$", ha='center', fontsize=9)

    ax.legend()
    buffer = BytesIO()
    fig.tight_layout()
    fig.savefig(buffer, format="png")
    buffer.seek(0)
    imagen_base64 = base64.b64encode(buffer.read()).decode("utf-8")
    plt.close(fig)
    return imagen_base64

def index(request):
    contexto = {
        'resultado': None,
        'error': None,
        'secciones': None,
        'grafica': None,
        'funcion': '',
        'a': '',
        'b': '',
        'n': '',
    }

    if request.method == 'POST':
        funcion = request.POST.get('funcion', '').strip()
        contexto['funcion'] = funcion

        try:
            a = float(request.POST.get('a', ''))
            b = float(request.POST.get('b', ''))
            n = int(request.POST.get('n', ''))
            contexto.update({'a': a, 'b': b, 'n': n})

            if n <= 0:
                contexto['error'] = "El número de subintervalos debe ser mayor que 0."
            elif a >= b:
                contexto['error'] = "El límite inferior debe ser menor que el límite superior."
            else:
                time.sleep(1.2)  # Simulación de cálculo
                resultado_detallado, error = trapecio_compuesto_detallado_educativo(funcion, a, b, n)
                if error:
                    contexto['error'] = error[0]
                elif resultado_detallado is None:
                    contexto['error'] = "Error al evaluar la función. Verifica la sintaxis."
                else:
                    grafica = generar_grafica(funcion, a, b, n)
                    contexto.update({
                        'resultado': resultado_detallado['resultado'],
                        'secciones': resultado_detallado['secciones'],
                        'grafica': grafica,
                    })
        except ValueError:
            contexto['error'] = "Por favor, ingresa valores numéricos válidos en los campos correspondientes."

    return render(request, 'integracion_compuesta/index.html', contexto)
