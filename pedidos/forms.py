from django import forms
from .models import Type

class PedidosForm(forms.Form):
    tipo_de_pedido = forms.ModelChoiceField(queryset = Type.objects.all())
    obs = forms.CharField(max_length = 100, required=False)