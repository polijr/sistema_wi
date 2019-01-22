from django import forms
from .models import *

class TransportadoraForm(forms.Form):
	nome = forms.CharField(required = True)
	CNPJ = forms.CharField(required = True, max_length=14)
	valor_maximo = forms.FloatField(required = True)
	regiao = forms.MultipleChoiceField(required = True)
	telefone = forms.CharField(required = True)
	email = forms.CharField(required = True)
	maximo_pedidos = forms.IntegerField(required = True)

class NotFisForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('arquivo',)

class RastreamentoForm(forms.ModelForm):
    class Meta:
        model = RastreamentoArquivo
        fields = ('arquivo',)

class TabelaPrecosForm(forms.ModelForm):
    class Meta:
        model = Tabela_Precos
        fields = ('arquivo',)

class TabelaPrazosForm(forms.ModelForm):
    class Meta:
        model = Tabela_Prazos
        fields = ('arquivo',)

# class RegraDeNegocioForm(forms.ModelForm):
class RegraDeNegocioForm(forms.ModelForm):
    class Meta:
        model = RegraDeNegocio
        fields = ('preco','prazo', 'performance')
        widgets = {'preco_capital': forms.HiddenInput(),
                   'prazo_capital': forms.HiddenInput(),
                   'performance_capital': forms.HiddenInput(),
                   'preco_interior': forms.HiddenInput(),
                   'prazo_interior': forms.HiddenInput(),
                   'performance_interior': forms.HiddenInput()}

class FuncionarioForm (forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('foto',)

class AdministradorForm (forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ('foto',)
