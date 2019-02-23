from django import forms
from .models import Usuario, Gerente, Organizador, Empresa, Caravaneiro
from django.contrib.auth.models import User




class CadastroEmpresaForm(forms.Form):
    organizador_resp = forms.ModelChoiceField(queryset=Organizador.objects.all(), required = True)  
    nome = forms.CharField(required = True)
    stand = forms.IntegerField(required = True)
    tamanho = forms.IntegerField(required = True)
    palestra = forms.BooleanField(required = True)
    cnpj = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    username = forms.CharField(min_length=4, required=True)
    password = forms.CharField(min_length=4, required=True)
    password2 = forms.CharField(min_length=4, required=True)	     
           
    def clean(self):
        cleaned_data = super(CadastroEmpresaForm, self).clean()
        username = cleaned_data.get('username')
        if username:
            if User.objects.filter(username=username).count()>0:
                raise forms.ValidationError("Username já foi pego!")
        email = cleaned_data.get('email')
        if email:
            if User.objects.filter(email=email) > 0:
                raise forms.ValidationError("Esse email já foi usado em outra conta!")   
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2:
            if password != password2:
                raise forms.ValidationError("Senhas diferentes!")
        return cleaned_data
    
    class Meta:
        model = Empresa
        fields = ['usuario', 'nome', 'stand', 'tamanho', 'palestra', 'organizador_resp', 'cnpj']



class CadastroOrganizadorForm(forms.Form):
    nome = forms.CharField(required = True)
    sobrenome = forms.CharField(required = True)
    telefone = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    username = forms.CharField(min_length=4, required = True)
    password = forms.CharField(min_length=4, required = True)
    password2 = forms.CharField(min_length=4, required = True)	     
           
    def clean(self):
        cleaned_data = super(CadastroOrganizadorForm, self).clean()
        username = cleaned_data.get('username')
        if username:
            if User.objects.filter(username=username).count()>0:
                raise forms.ValidationError("Username ja foi pego!")
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2:
            if password != password2:
                raise forms.ValidationError("Senhas diferentes!")
        print(self)
        return cleaned_data
    
    class Meta:
        model = Organizador
        fields = ['nome', 'sobrenome', 'telefone', 'email']

class CadastroCaravaneiroForm(forms.Form):
    nome = forms.CharField(required = True)
    sobrenome = forms.CharField(required = True)
    telefone = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    username = forms.CharField(min_length=4, required = True)
    password = forms.CharField(min_length=4, required = True)
    password2 = forms.CharField(min_length=4, required = True)	     
           
    def clean(self):
        cleaned_data = super(CadastroCaravaneiroForm, self).clean()
        username = cleaned_data.get('username')
        if username:
            if User.objects.filter(username=username).count()>0:
                print("Nome ja foi pego")
                raise forms.ValidationError("Username ja foi pego!")
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2:
            if password != password2:
                raise forms.ValidationError("Senhas diferentes!")
        print(self)
        return cleaned_data
    
    class Meta:
        model = Caravaneiro
        fields = ['nome', 'sobrenome', 'telefone', 'email']

class EditarGerenteForm(forms.Form):
    nome = forms.CharField(required = False)
    sobrenome = forms.CharField(required = False)
    telefone = forms.CharField(required = False)
    email = forms.EmailField(required = False)
    username = forms.CharField(min_length=4, required = False)
    password = forms.CharField(min_length=4, required = False)
    password2 = forms.CharField(min_length=4, required = False)	     
    pk = forms.IntegerField()

    def clean(self):
        cleaned_data = super(EditarGerenteForm, self).clean()
        username = cleaned_data.get('username')
        pk = int(cleaned_data.get('pk'))
        if username:
            if User.objects.filter(username=username).count()>0:
                print(User.objects.filter(username=username)[0])
                print(Gerente.objects.get(pk=pk).usuario.user)
                if not Gerente.objects.get(pk=pk).usuario.user ==  User.objects.filter(username=username)[0]:
                    print("Nome ja foi pego")
                    raise forms.ValidationError("Username ja foi pego!")
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        print(self)
        return cleaned_data
    
    class Meta:
        model = Gerente
        fields = ['nome', 'sobrenome', 'telefone', 'email', 'username', 'password']
    
class EditarCaravaneiroForm(forms.Form):
    nome = forms.CharField(required = False)
    sobrenome = forms.CharField(required = False)
    telefone = forms.CharField(required = False)
    email = forms.EmailField(required = False)
    username = forms.CharField(min_length=4, required = False)
    password = forms.CharField(min_length=4, required = False)
    password2 = forms.CharField(min_length=4, required = False)	     
    pk = forms.IntegerField()   
    
    def clean(self):
        cleaned_data = super(EditarCaravaneiroForm, self).clean()
        username = cleaned_data.get('username')
        pk = int(cleaned_data.get('pk'))
        if username:
            if User.objects.filter(username=username).count()>0:
                if not Caravaneiro.objects.get(pk=pk).usuario.user ==  User.objects.filter(username=username)[0]:
                    print("Nome ja foi pego")
                    raise forms.ValidationError("Username ja foi pego!")
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        print(self)
        return cleaned_data
    
    class Meta:
        model = Caravaneiro
        fields = ['nome', 'sobrenome', 'telefone', 'email']

class EditarOrganizadorForm(forms.Form):
    nome = forms.CharField(required = False)
    sobrenome = forms.CharField(required = False)
    telefone = forms.CharField(required = False)
    email = forms.EmailField(required = False)
    username = forms.CharField(min_length=4, required = False)
    password = forms.CharField(min_length=4, required = False)
    password2 = forms.CharField(min_length=4, required = False)	     
    pk = forms.IntegerField()  

    def clean(self):
        cleaned_data = super(EditarOrganizadorForm, self).clean()
        username = cleaned_data.get('username')
        pk = int(cleaned_data.get('pk'))
        if username:
            if User.objects.filter(username=username).count()>0:
                if not Organizador.objects.get(pk=pk).usuario.user ==  User.objects.filter(username=username)[0]:
                    print("Nome ja foi pego")
                    raise forms.ValidationError("Username ja foi pego!")
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2:
            if password != password2:
                raise forms.ValidationError("Senhas diferentes!")
        print(self)
        return cleaned_data
    
    class Meta:
        model = Organizador
        fields = ['nome', 'sobrenome', 'telefone', 'email']


class EditarEmpresaForm(forms.Form):
    organizador_resp = forms.ModelChoiceField(queryset=Organizador.objects.all(), required = False)  
    nome = forms.CharField(required = False)
    stand = forms.IntegerField(required = False)
    tamanho = forms.IntegerField(required = False)
    palestra = forms.BooleanField(required = False)
    cnpj = forms.CharField(required = False)
    email = forms.EmailField(required = False)
    username = forms.CharField(min_length=4, required=False)
    password = forms.CharField(min_length=4, required=False)
    password2 = forms.CharField(min_length=4, required=False)
    pk = forms.IntegerField()	     
           
    def clean(self):
        cleaned_data = super(EditarEmpresaForm, self).clean()
        username = cleaned_data.get('username')
        pk = int(cleaned_data.get('pk'))
        if username:
            if User.objects.filter(username=username).count()>0:
                if not Empresa.objects.get(pk=pk).usuario.user ==  User.objects.filter(username=username)[0]:
                    print("Nome ja foi pego")
                    raise forms.ValidationError("Username ja foi pego!")
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2:
            if password != password2:
                raise forms.ValidationError("Senhas diferentes!")
        return cleaned_data
    
    class Meta:
        model = Empresa
        fields = ['usuario', 'nome', 'stand', 'tamanho', 'palestra', 'organizador_resp', 'cnpj']

class ResetSenhaForm(forms.Form):
    password = forms.CharField(min_length=4, required=True)
    password2 = forms.CharField(min_length=4, required=True)

    def clean(self):
        cleaned_data = super(ResetSenhaForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2:
            if password != password2:
                raise forms.ValidationError("Senhas diferentes!")
        return cleaned_data

    class Meta:
        model = User
        fields = ['password', 'password2']
            
