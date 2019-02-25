from django import forms
from .models import Documento, NotaFiscal

class DocumentoForm(forms.ModelForm):
	nome = forms.CharField(max_length=100, required=True)
	arquivo = forms.FileField()
	observacao = forms.CharField(max_length=200, required=False)

	class Meta:
		model = Documento
		fields = ['nome', 'arquivo', 'observacao']

	def save(self, empresa, commit=True):
		documento = Documento()
		documento.nome = self.cleaned_data['nome']
		documento.arquivo = self.cleaned_data['arquivo']
		documento.observacao = self.cleaned_data['observacao']
		documento.empresa = empresa
		if commit:
			documento.save()
		return documento

class NotaForm(forms.ModelForm):
	nome = forms.CharField(max_length=100, required=True)
	arquivo = forms.FileField()
	observacao = forms.CharField(max_length=200, required=False)

	class Meta:
		model = NotaFiscal
		fields = ['nome', 'arquivo', 'observacao','empresa']
