from django import forms
from .models import Type
from sistema_wi.models import ValoresEstaticos
from usuarios.models import Usuario

class PedidosForm(forms.Form):
    tipo_de_pedido = forms.ModelChoiceField(queryset = Type.objects.all())
    obs = forms.CharField(max_length = 100, required=False)


class TypeForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    image = forms.ImageField(required=False)
    caravaneiro = forms.IntegerField(required=False)
    class Meta:
        model = Type
        fields = ['name', 'image', 'caravaneiro']

class ValoresMassagemForm(forms.Form):
    horario_massagem_inicio = forms.TimeField(required=True)
    horario_massagem_fim = forms.TimeField(required=True)
    intervalo_massagem = forms.IntegerField(required=True)
    n_salas = forms.IntegerField(required=True)

    def clean(self):
        cleaned_data = super(ValoresMassagemForm, self).clean()
        horario_massagem_inicio = cleaned_data.get('horario_massagem_inicio')
        horario_massagem_fim = cleaned_data.get('horario_massagem_fim')
        intervalo_massagem = cleaned_data.get('intervalo_massagem')
        n_salas = cleaned_data.get('n_salas')
        if horario_massagem_inicio and horario_massagem_fim and horario_massagem_inicio > horario_massagem_fim:
            raise forms.ValidationError('O inicio não pode ser depois do fim')
        if intervalo_massagem and intervalo_massagem < 0:
            raise forms.ValidationError('O intervalo de tempo não pode ser negativo')
        if n_salas and n_salas < 0:
            raise forms.ValidationError('O número de salas não pode ser negativo')

    class Meta:
        model = ValoresEstaticos
        fields = ['horario_massagem_inicio', 'horario_massagem_fim', 'intervalo_massagem', 'n_salas']


class AgendamentoForm(forms.Form):
    sala=forms.CharField(required=True)
    horario=forms.ChoiceField(required=True)