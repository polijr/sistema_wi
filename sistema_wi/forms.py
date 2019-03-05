from django import forms
from .models import *

class DataForm(forms.ModelForm):
    data = forms.DateField()
	    
    class Meta:
        model = dataFeed
        fields = ['data']



class LinkForm(forms.ModelForm):
    nome = forms.CharField(max_length=300, required=True)
    link = forms.CharField(required=True, max_length=1000)
    class Meta:
        model = LinkFeed
        fields = ['nome', 'link']



class ValoresEstaticosForm(forms.Form):
    ano_wi = forms.CharField(required = True)  
    nome_wifi = forms.CharField(required = True)
    senha_wifi = forms.CharField(required = True)
    data_de_inicio = forms.DateField(required = False)
    mapa_wi = forms.FileField(required = False)
    calendario_wi = forms.FileField(required = False)
