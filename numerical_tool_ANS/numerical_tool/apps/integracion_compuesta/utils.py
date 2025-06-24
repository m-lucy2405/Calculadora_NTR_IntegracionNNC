import numpy as np
from sympy import sympify, lambdify, Symbol

def integrar_compuesto_trapecio(funcion_str, a, b, n):
    x = Symbol('x')
    funcion_sym = sympify(funcion_str)
    f = lambdify(x, funcion_sym, modules=["numpy"])

    h = (b - a) / n
    suma = f(a) + f(b)

    pasos = [f"h = (b - a) / n = ({b} - {a}) / {n} = {h:.5f}"]
    pasos.append(f"f(a) + f(b) = f({a}) + f({b}) = {f(a):.5f} + {f(b):.5f} = {suma:.5f}")

    for i in range(1, n):
        xi = a + i * h
        fx = f(xi)
        suma += 2 * fx
        pasos.append(f"f({xi:.5f}) = {fx:.5f} → suma parcial = {suma:.5f}")

    resultado = (h / 2) * suma
    pasos.append(f"Resultado final = (h/2) * suma = ({h}/2) * {suma:.5f} = {resultado:.5f}")
    return resultado, pasos
