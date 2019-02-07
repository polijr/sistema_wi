from django import forms
from .models import Informe

class InformeForm(forms.ModelForm):
    titulo = forms.CharField(max_length=100, required=True)
    texto = forms.CharField(required=True)
    class Meta:
        model = Informe
        fields = ['titulo', 'texto']


