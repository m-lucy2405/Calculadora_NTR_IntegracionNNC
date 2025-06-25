from sympy import symbols, sympify, diff
import numpy as np

# Logica para el método de Newton-Raphson

def newton_raphson_method(expr_str, x0, tol=1e-6, max_iter=100):
    x = symbols('x')
    f = sympify(expr_str)
    f_prime = diff(f, x)

    iterations = []
    xi = x0

    for i in range(max_iter):
        fxi = f.evalf(subs={x: xi})
        fpxi = f_prime.evalf(subs={x: xi})

        if fpxi == 0:
            break  # Evita división por cero

        xi_next = xi - (fxi / fpxi)
        error = abs(xi_next - xi)

        iterations.append({
            'iter': i + 1,
            'xi': float(xi),
            'f_xi': float(fxi),
            'f_prime_xi': float(fpxi),
            'xi_next': float(xi_next),
            'error': float(error)
        })

        if error < tol:
            return iterations, True  # Converge

        xi = xi_next

    return iterations, False  # No converge
