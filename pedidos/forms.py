from django import forms
from .models import Type

class PedidosForm(forms.Form):
    tipo_de_pedido = forms.ModelChoiceField(queryset = Type.objects.all())
    obs = forms.CharField(max_length = 100, required=False)


class TypeForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    image = forms.ImageField()
    class Meta:
        model = Type
        fields = ['name', 'image']