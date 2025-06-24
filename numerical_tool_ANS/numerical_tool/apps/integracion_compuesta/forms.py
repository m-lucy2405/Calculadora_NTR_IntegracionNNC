from django import forms

class IntegracionForm(forms.Form):
    funcion = forms.CharField(
        label='Función f(x)',
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: x**2 + 1'
        })
    )
    a = forms.FloatField(
        label='Límite inferior (a)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    b = forms.FloatField(
        label='Límite superior (b)',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    n = forms.IntegerField(
        label='Subintervalos (n)',
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )