from django import forms
from .models import Usuario, Gerente, Organizador, Empresa
from django.contrib.auth.models import User




class CadastroEmpresaForm(forms.Form):
    organizador_resp = forms.ModelChoiceField(queryset=Organizador.objects.all(), required = True)  
    nome = forms.CharField(required = True)
    stand = forms.IntegerField(required = True)
    tamanho = forms.IntegerField(required = True)
    palestra = forms.BooleanField(required = True)
    cnpj = forms.CharField(required = True)
    email = forms.CharField(required = True)
    username = forms.CharField(min_length=4)
    password = forms.CharField(min_length=4, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=4, widget=forms.PasswordInput)	     
           
    def clean(self):
        cleaned_data = super(CadastroEmpresaForm, self).clean()
        username = cleaned_data.get('username')
        if username:
            if User.objects.get(username=username):
                raise forms.ValidationError("Username ja foi pego!")
                return cleaned_data
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2:
            if password != password2:
                raise forms.ValidationError("Senhas diferentes!")
        return cleaned_data
    
    class Meta:
        model = Empresa
        fields = ['usuario', 'nome', 'stand', 'tamanho', 'palestra', 'organizador_resp', 'cnpj']
