from django import form

class PedidosForm(forms.Form):
    tipo_de_pedido = form.ModelChoiceField(queryset = Type.objects.all())
    obs = form.CharField(max_length = 100)