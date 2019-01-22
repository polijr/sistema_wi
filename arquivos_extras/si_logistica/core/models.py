from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from django.contrib.postgres.fields import ArrayField

from datetime import datetime 
import calendar
import datetime
from datetime import date
from django.contrib.auth.models import User


# ---------------------------------
# -------- TRANSPORTADORA ----------
class Transportadora(models.Model):
    nome = models.CharField(max_length=300)
    CNPJ = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
#    sede = models.CharField(max_length=100)
    telefone = models.CharField(max_length=16, blank='True')
    valorMaximo = models.FloatField(null=True, blank='True')
    valorAtual = models.FloatField(null=True, default = 0)
    maximoPedidos = models.IntegerField(null=True, blank='True')
    quantidadeAtual = models.IntegerField(null=True, default = 0)
    logo = models.ImageField(upload_to='media/transportadoras', default='media/transportadoras/default.png')
    preco = models.FloatField(null=True, blank='True')
    # prazo = models.ForeignKey(Prazo, on_delete=models.CASCADE, null=True)
    performance = models.IntegerField(null=True, blank='True', default=100)
    rankingPreco = models.FloatField(null=True, blank='True')
    rankingPrazo = models.FloatField(null=True, blank='True')
    rankingPerformance = models.FloatField(null=True, blank='True')
    rankingGeral = models.FloatField(null=True, blank='True')
    regiaoDeAtuacao = models.CharField(max_length=10, null=True, blank='True')
    adValorem = models.FloatField(default=0.0)

    SUL = "SUL"
    SUDESTE = "SUDESTE"
    CENTROOESTE = "CENTROOESTE"
    NORTE = "NORTE"
    NORDESTE = "NORDESTE"

    REGIAO_CHOICES = (
        (SUL, "Sul"),
        (SUDESTE, "Sudeste"),
        (CENTROOESTE, "Centro-Oeste"),
        (NORTE, "Norte"),
        (NORDESTE, "Nordeste"),
    )

    regiao = MultiSelectField(max_length=120, choices = REGIAO_CHOICES, default=SUL, max_choices=5)
    # arquivo = models.FileField(upload_to='arquivos/')



#---------------------------------------------
#------------------ PRAZO --------------------
class Prazo(models.Model):
    REGIAO_CHOICES = (
        ('C', 'Capital'),
        ('I', 'Interior'),
    )

    nome = models.CharField(max_length=100)
    UF = models.CharField(max_length=2)
    inicioCEP = models.CharField(max_length=8)
    fimCEP = models.CharField(max_length=8)
    prazoSEDEX = models.IntegerField()
    prazoPAC = models.IntegerField()
    regiao = models.CharField(max_length=1, choices=REGIAO_CHOICES)
    transportadora = models.ForeignKey(Transportadora, on_delete=models.CASCADE, null=True)
#---------------------------------------------
#--------------- VALORES ---------------------
class Valor(models.Model):
    valor = models.FloatField()
    capital_interior = models.CharField(max_length=2)
    peso = models.IntegerField()
    estado = models.CharField(max_length=20)
    origem = models.CharField(max_length=2)
    regiaoDeAtuacao = models.CharField(max_length=10, )
    transportadora = models.ForeignKey(Transportadora, on_delete=models.CASCADE, null=True)


#---------------------------------------------
#--------------- TABELAS ---------------------
class Tabela_Precos(models.Model):
    arquivo = models.FileField(upload_to='core/static/media/TabelaPreco/')
    transportadora = models.ForeignKey(Transportadora, on_delete=models.CASCADE, null=True)

class Tabela_Prazos(models.Model):
    arquivo = models.FileField(upload_to='core/static/media/TabelaPrazo/')
    transportadora = models.ForeignKey(Transportadora, on_delete=models.CASCADE, null=True) 
    
class Tabela_Interior_Interior(models.Model):
    valor = models.FloatField()
    peso = models.IntegerField()
    estado = models.CharField(max_length = 20)
    transportadora = models.ForeignKey(Transportadora, on_delete=models.CASCADE)

class Tabela_Interior_Capital(models.Model):
    valor = models.FloatField()
    peso = models.IntegerField()
    estado = models.CharField(max_length = 20)
    transportadora = models.ForeignKey(Transportadora, on_delete=models.CASCADE)

class Tabela_Capital_Interior(models.Model):
    valor = models.FloatField()
    peso = models.IntegerField()
    estado = models.CharField(max_length = 20)
    transportadora = models.ForeignKey(Transportadora, on_delete=models.CASCADE)

class Tabela_Capital_Capital(models.Model):
    valor = models.FloatField()
    peso = models.IntegerField()
    estado = models.CharField(max_length = 20)
    transportadora = models.ForeignKey(Transportadora, on_delete=models.CASCADE)

#---------------------------------------------
#--------------- REGISTRO --------------------
class Registro(models.Model):
    identificacao = models.CharField(max_length = 100)
    data = models.DateField(auto_now_add=True, blank=True, null=True)
    arquivo = models.FileField(upload_to='core/arquivos/', null=True)

#---------------------------------------------
#--------------- PEDIDO ----------------------
class Pedido(models.Model):
    REGIAO_CHOICES = (
        ('C', 'Capital'),
        ('I', 'Interior'),
    )
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Entregue', 'Entregue'),
        ('Encaminhado', 'Encaminhado')
    )
    identificacao = models.CharField(max_length=200)
    codigo = models.CharField(max_length=16, null=True)
    valor = models.FloatField(max_length=200)
    peso = models.FloatField(max_length=32, default=0.0)
    origem = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    #empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    transportadora = models.ForeignKey(Transportadora, on_delete=models.CASCADE, null=True)
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE)
    UFDestino = models.CharField(max_length=2)
    regiaoDestino = models.CharField(max_length=1, choices=REGIAO_CHOICES)
    cliente = models.CharField(max_length=30, blank = True)
    data_conemb = models.DateField(auto_now=True)
    data_ocoren = models.DateField(auto_now=True)
    data_previsao = models.DateField(auto_now=True)
    prazo = models.IntegerField(default=0)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default='Pendente')



#---------------------------------------------
#-------- REGRA DE NEGOCIO -------------------
class RegraDeNegocio(models.Model):
    REGIAO_CHOICES = (
        ('C', 'Capital'),
        ('I', 'Interior'),
    )

    identificacao = models.CharField(max_length=200)
    UF = models.CharField(max_length=2)
    regiao = models.CharField(max_length=1, choices=REGIAO_CHOICES)
    preco = models.IntegerField(null=True)
    prazo = models.IntegerField(null=True)
    performance = models.IntegerField(null=True)


#---------------------------------------------
#--------- PROGRAMAÇÃO TRANSPORTE ------------
class ProgramacaoTransporte(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=False, related_name='programacao_transporte')
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE, null=False)
    transportadora = models.ForeignKey(Transportadora, on_delete=models.SET_NULL, null=True)
    # regraDeNegocio = models.ForeignKey(RegraDeNegocio, on_delete=models.CASCADE, null=True)
    data = models.DateField(auto_now=True)
    prazoEstimado = models.IntegerField(default = 0, null=True)
    precoEstimado = models.FloatField(default = 0, null=True) 

class RastreamentoArquivo(models.Model):
    TIPO_CHOICES = (
        ('CONEMB', 'CONEMB'),
        ('OCOREN', 'OCOREN'),
    )
    STATUS_CHOICES = (
        ('Finalizado', 'FINALIZADO'),
        ('Problema na Entrega', 'PROBLEMA NA ENTREGA'),
        ('Encaminhado', 'ENCAMINHADO')
    )

    data = models.CharField(max_length=16)
    tipo = models.CharField(max_length=8, choices=TIPO_CHOICES)
    codigo = models.CharField(max_length=8)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES)
    arquivo = models.FileField(upload_to='core/static/media/Rastreamento/')



#---------------------------------------------
#--------- ATORES ------------

class Funcionario(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=200)
    senha = models.CharField(max_length=50)
    confirmar_senha = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    foto = models.FileField("Foto", upload_to='core/static/media/Fotos_Perfil/', null=True, blank=True)
    

class Administrador(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=200)
    senha = models.CharField(max_length=50)
    confirmar_senha = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    foto = models.FileField("Foto", upload_to='core/static/media/Fotos_Perfil/', null=True, blank=True)


class Proprietario(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=200)
    senha = models.CharField(max_length=50)
    confirmar_senha = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    foto = models.FileField("Foto", upload_to='core/static/media/Fotos_Perfil/', null=True, blank=True)

