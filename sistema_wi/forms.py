from django import forms
from .models import dataFeed

class DataForm(forms.ModelForm):
    data = forms.DateField()
    link = forms.CharField(max_length=100, required=True)
	    
    class Meta:
        model = dataFeed
        fields = ['data', 'link']