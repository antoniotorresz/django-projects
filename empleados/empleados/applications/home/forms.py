from django import forms

from empleados.applications.home.models import Prueba


class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        fields = ('titulo', 'subtitulo')
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su texto aqui'
                }
            )
        }
    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if len(titulo) < 5:
            raise forms.ValidationError('Ingrese un titulo de mas 5 caracteres')
        return titulo