from django import forms

class IntegracionForm(forms.Form):
    funcion = forms.CharField(label='Función f(x)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    a = forms.FloatField(label='Límite inferior a', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    b = forms.FloatField(label='Límite superior b', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    n = forms.IntegerField(label='Número de subintervalos n (par)', min_value=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def clean_n(self):
        n = self.cleaned_data.get('n')
        if n % 2 != 0:
            raise forms.ValidationError("n debe ser un número par para el método compuesto.")
        return n
