from django import forms

# Formulario para validar el método de Newton-Raphson

class NewtonRaphsonForm(forms.Form):
    funcion = forms.CharField(
        label='f(x)',
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: x**2 - 2'})
    )
    valor_inicial = forms.FloatField(
        label='Valor inicial (x₀)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 1.0'})
    )
    tolerancia = forms.FloatField(
        label='Tolerancia',
        initial=0.000001,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 0.000001'})
    )
    iteraciones = forms.IntegerField(
        label='Máximo de iteraciones',
        initial=100,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 100'})
    )

    def clean_funcion(self):
        data = self.cleaned_data['funcion']
        try:
            from sympy import sympify
            sympify(data)
        except:
            raise forms.ValidationError("La función ingresada no es válida.")
        return data