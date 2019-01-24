from django import forms
from .models import Usuario, Gerente, Organizador, empresa
from .choices import *



class CadastroEmpresaForm(forms.Form):
    organizador_resp = models.ForeignKey(Organizador, on_delete = models.CASCADE, required = True)  
    nome = forms.CharField(required = True)
    stand = models.IntegerField(required = True)
    CNPJ = forms.CharField(required = True, max_length=14)
    tamanho = forms.ChoiceField(choices = TAMANHO_CHOICES , required = True)
    palestra = forms.BooleanField(required = True)
    cnpj = forms.CharField(required = True)
    email = forms.CharField(required = True)
    senha = forms.CharField(widget=forms.PasswordInput)
    senha2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)	     
           
    def clean_senha2(self):
        # Ver se as 2 senhas batem
        senha = self.cleaned_data.get("senha")
        senha2 = self.cleaned_data.get("senha2")
        if senha and senha2 and senha != senha2:
            raise forms.ValidationError("As senhas são diferentes")
        return senha2
