from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'


class LibroBusquedaForm(forms.Form):
    busqueda = forms.CharField(label='Buscar libro por titulo', required=False)