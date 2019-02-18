from django import forms


class ValoresEstaticosForm(forms.Form):
    ano_wi = forms.CharField(required = True)  
    nome_wifi = forms.CharField(required = True)
    senha_wifi = forms.CharField(required = True)
    data = forms.DateTimeField(required = True)
    mapa_wi = forms.ImageField(required = False)