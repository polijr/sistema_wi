from django import forms
<<<<<<< HEAD
from .models import dataFeed

class DataForm(forms.ModelForm):
    data = forms.DateField()
    link = forms.CharField(max_length=100, required=True)
	    
    class Meta:
        model = dataFeed
        fields = ['data', 'link']
=======


class ValoresEstaticosForm(forms.Form):
    ano_wi = forms.CharField(required = True)  
    nome_wifi = forms.CharField(required = True)
    senha_wifi = forms.CharField(required = True)
    data = forms.DateField(required = True)
    mapa_wi = forms.ImageField(required = True)
>>>>>>> baf139ee0c9fb32312fc37f08b34647f21423dca
