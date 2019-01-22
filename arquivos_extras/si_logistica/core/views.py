from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.apps import apps
from .models import *
from .forms import *
from django.apps import apps
import xlwt
from django.core.mail import send_mail
import pandas
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
import os
import xlsxwriter
from django.http import HttpResponse
from operator import attrgetter
from .excel import *
import datetime
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import pdfkit
from django.conf import settings
from django.contrib.auth.forms import UserChangeForm

import datetime
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import pdfkit


def DeterminaRegiao(cep):
    cep = int(cep)

    if cep >= 1000000 and cep <= 39999999:
        regiao = "SUDESTE"
    elif cep >= 40000000 and cep <= 65999999:
        regiao = "NORDESTE"
    elif cep >= 66000000 and cep <= 69999999:
        regiao = "NORTE"
    elif cep >= 76800000 and cep <= 77999999:
        regiao = "NORTE"
    elif cep >= 70000000 and cep <= 76799999:
        regiao = "CENTROOESTE"
    elif cep >= 78000000 and cep <= 79999999:
        regiao = "CENTROOESTE"
    elif cep >= 80000000 and cep <= 99999999:
        regiao = "SUL"
    else:
        regiao = "ERRO"

    return regiao

def DeterminaEstado(cep):
    cep = int(cep)

    if cep >= 1000000 and cep <= 19999999:
        estado = "SP"
    elif cep >= 2000000 and cep <= 28999999:
        estado = "RJ"
    elif cep >= 2900000 and cep <= 29999999:
        estado = "ES"
    elif cep >= 30000000 and cep <= 39999999:
        estado = "MG"
    elif cep >= 40000000 and cep <= 48999999:
        estado = "BA"
    elif cep >= 49000000 and cep <= 49999999:
        estado = "SE"
    elif cep >= 50000000 and cep <= 56999999:
        estado = "PE"
    elif cep >= 57000000 and cep <= 57999999:
        estado = "AL"
    elif cep >= 40000000 and cep <= 48999999:
        estado = "BA"
    elif cep >= 58000000 and cep <= 58999999:
        estado = "PB"
    elif cep >= 59000000 and cep <= 59999999:
        estado = "RN"
    elif cep >= 60000000 and cep <= 63999999:
        estado = "CE"
    elif cep >= 64000000 and cep <= 64999999:
        estado = "PI"
    elif cep >= 64000000 and cep <= 65999999:
        estado = "MA"
    elif cep >= 66000000 and cep <= 68899999:
        estado = "PA"
    elif cep >= 68900000 and cep <= 68999999:
        estado = "AP"
    elif cep >= 69000000 and cep <= 69899999:
        estado = "AM"
    elif cep >= 69300000 and cep <= 69300000:
        estado = "RR"
    elif cep >= 69900000 and cep <= 69999999:
        estado = "AC"
    elif cep >= 70000000 and cep <= 73699999:
        estado = "DF"
    elif cep >= 74000000 and cep <= 76799999:
        estado = "GO"
    elif cep >= 77000000 and cep <= 77995999:
        estado = "TO"
    elif cep >= 78000000 and cep <= 78899999:
        estado = "MT"
    elif cep >= 78900000 and cep <= 78999999:
        estado = "RO"
    elif cep >= 80000000 and cep <= 87999999:
        estado = "PR"
    elif cep >= 88000000 and cep <= 89999999:
        estado = "SC"
    elif cep >= 90000000 and cep <= 99999999:
        estado = "RS"
    else:
        estado = "XX"

    return estado

# ----------------------------------
# ------- VIEWS DE HOME ------------
# ----------------------------------

class Home(View):
    def get (self, request, *args, **kwargs):
        return render(request, "dashboard.html")



# ---------------------------------------
# -------- VIEWS DE TRANSPORTADORA ------
# ---------------------------------------

# Cadastrar Transportadora
class CadastrarTransportadora(View): 
    template_name = 'criar_transportadora.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'erro': False})
    def post(self, request, *args, **kwargs):
        try:
            transportadora = Transportadora.objects.create(
                nome=request.POST.get('nome'),
                CNPJ=request.POST.get('CNPJ'),
                email=request.POST.get('email'),
                telefone=request.POST.get('telefone'),
            )
            transportadora.save()
            transportadora_pk = transportadora.pk
        except:
            return render(request, self.template_name, {'erro': True})

        return redirect('/transportadora/'+  str(transportadora_pk)  +'/dados')


# 
class TransportadoraDados(View):
    template_name = 'criar_transportadora_dados.html'
    def get(self, request, pk, *args, **kwargs):
        transportadora = Transportadora.objects.get(pk=pk)
        context = {}
        context['transportadora'] = transportadora
        return render(request, self.template_name, context)
    def post(self, request, pk, *args, **kwargs):
        transportadora = Transportadora.objects.get(pk=pk)
        transportadora.regiao = request.POST.get('regiao')
        transportadora.maximoPedidos = request.POST.get('maximo_pedidos')
        transportadora.valorMaximo = request.POST.get('valor_maximo')
        transportadora.save()
        transportadora_pk = transportadora.pk
        
        return redirect('/transportadora/'+  str(transportadora_pk)  +'/uploads')

# 
class TransportadoraUploads(View):
    template_name = 'criar_transportadora_uploads.html'
    def get(self, request, pk, *args, **kwargs):
        transportadora = Transportadora.objects.get(pk=pk)
        context = {}
        context['transportadora'] = transportadora
        return render(request, self.template_name, context)
    def post(self, request, pk, *args, **kwargs):
        transportadora = Transportadora.objects.get(pk=pk)
        transportadora_pk = pk
        
        form = TabelaPrecosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        tabelaPreco(transportadora_pk)

        return redirect('/transportadora/'+  str(transportadora_pk)  +'/uploads_prazo')

class TransportadoraUploadsPrazo(View):
    template_name = 'criar_transportadora_uploads_prazo.html'
    def get(self, request, pk, *args, **kwargs):
        transportadora = Transportadora.objects.get(pk=pk)
        context = {}
        context['transportadora'] = transportadora
        return render(request, self.template_name, context)
    def post(self, request, pk, *args, **kwargs):
        transportadora = Transportadora.objects.get(pk=pk)
        transportadora_pk = pk
        # UPLOAD AQUI
        
        form = TabelaPrazosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        leTabelaPrazo(transportadora_pk)

        return redirect('/transportadoras')

# Listar Transportadora
class ListarTransportadoras(View):
    template_name = "listar_transportadoras.html"
    def get(self, request):
        context = {}
        context['lista_transportadoras'] = Transportadora.objects.all()
        return render(request, self.template_name, context)

    def post(self, request):
        return render(request, self.template_name, context)

# Ver Transportadora
class VerTransportadora(View):
    template_name = "ver_transportadora.html"
    def get(self, request, transportadora_id):
        context = {}
        transportadora = Transportadora.objects.get(id=transportadora_id)
        context['transportadora'] = Transportadora.objects.get(id=transportadora_id)
        # context['tabelaPreco'] = Tabela_Precos.objects.get(transportadora=transportadora)
        # context['tabelaPrazo'] = Tabela_Prazos.objects.get(transportadora=transportadora)
        return render(request, self.template_name, context)
    def post(self, request, transportadora_id):
        return render(request, self.template_name, context)

# Editar Transportadora
class EditarTransportadora(View):
    template_name = "alterar_transportadora.html"
    def get(self, request, pk):
        context = {}
        context['transportadora'] = Transportadora.objects.get(pk=pk)
        return render(request, self.template_name, context)

    def post(self, request, pk):
        transportadora = Transportadora.objects.get(pk=pk)
        transportadora.nome = request.POST.get('nome')
        transportadora.CNPJ = request.POST.get('CNPJ')
        transportadora.email = request.POST.get('email')
        transportadora.telefone = request.POST.get('telefone')

        transportadora.save()
        transportadora_pk = transportadora.pk

        return redirect('/transportadora/'+  str(transportadora_pk)  +'/dados')





# -----------------------------------
# ------- VIEWS DE PEDIDOS ----------
# -----------------------------------

# Criar Pedidos
class CriarPedido(View): 
    template_name = 'criar_pedidos.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):
        transportadora = Transportadora.objects.create(
            nome=request.POST.get('nome'),
            CNPJ=request.POST.get('CNPJ'),
        )
        transportadora.save()
        
        return render(request, self.template_name, {'form' : form})
class ListaPedidos(ListView):
    template_name = "rastreamento.html"
    def get(self, request):
        context = {}
        context['rastreamento_pedidos'] = Pedido.objects.all()
        return render(request, self.template_name, context)

    def post(self, request):
        return render(request, self.template_name, context)


class VerPedido(DetailView):
    template_name = "ver_pedido.html"
    def get(self, request, pk):
        pedido = Pedido.objects.get(pk=pk)
        
        context = {}
        context['pedido'] = pedido

        return render(request, self.template_name, context)
    def post(self, request, pk):
        return render(request, self.template_name, context)

class VerRegistro(View):
    template_name = "ver_registro.html"
    def get(self, request, pk):
        registro = Registro.objects.get(pk=pk)
        pedidos = Pedido.objects.filter(registro = registro)

        context = {}
        context['registro'] = registro
        context['pedidos'] = pedidos

        return render(request, self.template_name, context)
    def post(self, request, pk):
        return render(request, self.template_name, context)
# class CriarPedido(CreateView):
#     model = Pedido
#     fields = ['identificacao', 'valor', 'origem', 'destino', 'empresa', 'transportadora']
#     success_url = reverse_lazy('lista_pedidos')

# class AlteraPedido(UpdateView):
#     model = Pedido
#     fields = ['identificacao', 'valor', 'origem', 'destino', 'empresa', 'transportadora']
#     success_url = reverse_lazy('lista_pedidos')

# class DeletaPedido(DeleteView):
#     model = Pedido
#     success_url = reverse_lazy('lista_pedidos')

# class ListaRegraDeNegocio(ListView):
#     model = RegraDeNegocio

class ListaRegraDeNegocio(ListView):
    template_name = "regra_de_negocio.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        context = {}
        if request.method == "POST":
            estado = request.POST['estados']
            status_form = RegraDeNegocioForm(request.POST)
            if status_form.is_valid():
                status_form.save()
            # teste = request.POST['valor-prazo-interior']
            precoCap = 10
            prazoCap = 20
            performanceCap = 70
            precoInt = 50
            prazoInt = 40
            performanceInt = 10

            
            if estado == 'ALL':
                RegraDeNegocio.objects.all().delete()
                RegraDeNegocio.objects.create(identificacao='', UF='AC', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='AL', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='AP', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='AM', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='BA', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='CE', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='DF', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='ES', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='GO', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='MA', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='MT', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='MS', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='MG', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='PA', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='PB', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='PR', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='PE', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='PI', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='RJ', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='RS', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='RN', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='RO', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='RR', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='SC', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='SP', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='SE', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                RegraDeNegocio.objects.create(identificacao='', UF='TO', regiao='C', preco=precoCap, prazo=prazoCap, performance=performanceCap)
                
                RegraDeNegocio.objects.create(identificacao='', UF='AC', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='AL', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='AP', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='AM', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='BA', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='CE', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='DF', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='ES', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='GO', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='MA', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='MT', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='MS', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='MG', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='PA', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='PB', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='PR', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='PE', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='PI', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='RJ', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='RS', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='RN', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='RO', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='RR', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='SC', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='SP', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='SE', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
                RegraDeNegocio.objects.create(identificacao='', UF='TO', regiao='I', preco=precoInt, prazo=prazoInt, performance=performanceInt)
            
            # if estado == 'AC':
            #     RegraDeNegocio.objects.create(identificacao='', UF='AC', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='AC', regiao='I', preco, prazo, performance)
            # if estado == 'AL':
            #     RegraDeNegocio.objects.create(identificacao='', UF='AL', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='AL', regiao='I', preco, prazo, performance)
            # if estado == 'AP':
            #     RegraDeNegocio.objects.create(identificacao='', UF='AP', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='AP', regiao='I', preco, prazo, performance)
            # if estado == 'AM':
            #     RegraDeNegocio.objects.create(identificacao='', UF='AM', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='AM', regiao='I', preco, prazo, performance)
            # if estado == 'BA':
            #     RegraDeNegocio.objects.create(identificacao='', UF='BA', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='BA', regiao='I', preco, prazo, performance)
            # if estado == 'CE':
            #     RegraDeNegocio.objects.create(identificacao='', UF='CE', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='CE', regiao='I', preco, prazo, performance)
            # if estado == 'DF':
            #     RegraDeNegocio.objects.create(identificacao='', UF='DF', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='DF', regiao='I', preco, prazo, performance)
            # if estado == 'ES':
            #     RegraDeNegocio.objects.create(identificacao='', UF='ES', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='ES', regiao='I', preco, prazo, performance)
            # if estado == 'GO':
            #     RegraDeNegocio.objects.create(identificacao='', UF='GO', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='GO', regiao='I', preco, prazo, performance)
            # if estado == 'MA':
            #     RegraDeNegocio.objects.create(identificacao='', UF='MA', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='MA', regiao='I', preco, prazo, performance)
            # if estado == 'MT':
            #     RegraDeNegocio.objects.create(identificacao='', UF='MT', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='MT', regiao='I', preco, prazo, performance)
            # if estado == 'MS':
            #     RegraDeNegocio.objects.create(identificacao='', UF='MS', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='MS', regiao='I', preco, prazo, performance)
            # if estado == 'MG':
            #     RegraDeNegocio.objects.create(identificacao='', UF='MG', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='MG', regiao='I', preco, prazo, performance)
            # if estado == 'PA':
            #     RegraDeNegocio.objects.create(identificacao='', UF='PA', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='PA', regiao='I', preco, prazo, performance)
            # if estado == 'PB':
            #     RegraDeNegocio.objects.create(identificacao='', UF='PB', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='PB', regiao='I', preco, prazo, performance)
            # if estado == 'PR':
            #     RegraDeNegocio.objects.create(identificacao='', UF='PR', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='PR', regiao='I', preco, prazo, performance)
            # if estado == 'PE':
            #     RegraDeNegocio.objects.create(identificacao='', UF='PE', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='PE', regiao='I', preco, prazo, performance)
            # if estado == 'PI':
            #     RegraDeNegocio.objects.create(identificacao='', UF='PI', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='PI', regiao='I', preco, prazo, performance)
            # if estado == 'RJ':
            #     RegraDeNegocio.objects.create(identificacao='', UF='RJ', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='RJ', regiao='I', preco, prazo, performance)
            # if estado == 'RS':
            #     RegraDeNegocio.objects.create(identificacao='', UF='RS', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='RS', regiao='I', preco, prazo, performance)
            # if estado == 'RN':
            #     RegraDeNegocio.objects.create(identificacao='', UF='RN', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='RN', regiao='I', preco, prazo, performance)
            # if estado == 'RO':
            #     RegraDeNegocio.objects.create(identificacao='', UF='RO', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='RO', regiao='I', preco, prazo, performance)
            # if estado == 'RR':
            #     RegraDeNegocio.objects.create(identificacao='', UF='RR', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='RR', regiao='I', preco, prazo, performance)
            # if estado == 'SC':
            #     RegraDeNegocio.objects.create(identificacao='', UF='SC', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='SC', regiao='I', preco, prazo, performance)
            # if estado == 'SP':
            #     RegraDeNegocio.objects.create(identificacao='', UF='SP', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='SP', regiao='I', preco, prazo, performance)
            # if estado == 'SE':
            #     RegraDeNegocio.objects.create(identificacao='', UF='SE', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='SE', regiao='I', preco, prazo, performance)
            # if estado == 'TO':
            #     RegraDeNegocio.objects.create(identificacao='', UF='TO', regiao='C', preco, prazo, performance)
            #     RegraDeNegocio.objects.create(identificacao='', UF='TO', regiao='I', preco, prazo, performance)
            
        return render(request, self.template_name, context)

# class CriarRegraDeNegocio(CreateView):
#     model = RegraDeNegocio
#     fields = ['identificacao', 'inicioCEP', 'fimCEP', 'preco', 'prazo','performance']
#     success_url = reverse_lazy('lista_regras')

# class AlteraRegraDeNegocio(UpdateView):
#     model = RegraDeNegocio
#     fields = ['identificacao', 'inicioCEP', 'fimCEP', 'preco', 'prazo','performance']
#     success_url = reverse_lazy('lista_regras')

# class DeletaRegraDeNegocio(DeleteView):
#     model = RegraDeNegocio
#     success_url = reverse_lazy('lista_regras')
    

class ListaRegistro(ListView):
    template_name = "listar_registro.html"
    def get(self, request):
        context = {}
        context['registros'] = Registro.objects.all()
        return render(request, self.template_name, context)

    def post(self, request):
        return render(request, self.template_name, context)

class VerRegistro(View):
    template_name = "ver_registro.html"
    def get(self, request, pk):

        registro = Registro.objects.get(pk=pk)
        pedidos = Pedido.objects.filter(registro = registro)

        context = {}
        context['registro'] = registro
        context['pedidos'] = pedidos

        return render(request, self.template_name, context)
    def post(self, request, pk):
        return render(request, self.template_name, context)

class CriarRegistro(View): 
    template_name = 'criar_registro.html'
    def get(self, request, *args, **kwargs):
        context = {
            'erro': False,
            'success': False,
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        erro, success = False, False

        if "Text" in request.POST:
            try:
                form = NotFisForm(request.POST, request.FILES)
                if form.is_valid():
                    pk = ImportarNotFis(request)
                    success = True
                else:
                    erro = True
            except:
                erro = True

        elif "Excel" in request.POST:
            try:
                form = NotFisForm(request.POST, request.FILES)
                if form.is_valid():
                    pk = ImportarRegistroExcel(request)
                    success = True
                else:
                    erro = True
            except:
                erro = True            

        context = {'erro': erro,
                   'success': success,
                   'form': form,
        }

        return redirect('/registros/ver/' + str(pk))

class CriarRegistroNotFis(View): 
    template_name = 'criar_registro_notfis.html'
    def get(self, request, *args, **kwargs):
        context = {
            'erro': False,
            'success': False,
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        erro, success = False, False

        if "Text" in request.POST:
            try:
                form = NotFisForm(request.POST, request.FILES)
                if form.is_valid():
                    pk = ImportarNotFis(request)
                    success = True
                else:
                    erro = True
            except:
                erro = True

        elif "Excel" in request.POST:
            try:
                form = NotFisForm(request.POST, request.FILES)
                if form.is_valid():
                    pk = ImportarRegistroExcel(request)
                    success = True
                else:
                    erro = True
            except:
                erro = True            

        context = {'erro': erro,
                   'success': success,
                   'form': form,
        }

        return redirect('/registros/ver/' + str(pk))

class CriarRegistroExcel(View): 
    template_name = 'criar_registro_excel.html'
    def get(self, request, *args, **kwargs):
        context = {
            'erro': False,
            'success': False,
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        erro, success = False, False

        if "Text" in request.POST:
            try:
                form = NotFisForm(request.POST, request.FILES)
                if form.is_valid():
                    pk = ImportarNotFis(request)
                    success = True
                else:
                    erro = True
            except:
                erro = True

        elif "Excel" in request.POST:
            try:
                form = NotFisForm(request.POST, request.FILES)
                if form.is_valid():
                    pk = ImportarRegistroExcel(request)
                    success = True
                else:
                    erro = True
            except:
                erro = True            

        context = {'erro': erro,
                   'success': success,
                   'form': form,
        }

        return redirect('/registros/ver/' + str(pk))


class AlteraRegistro(UpdateView):
    model = Registro
    fields = ['identificação']
    success_url = reverse_lazy('registros')

class DeletaRegistro(DeleteView):
    model = Registro
    success_url = reverse_lazy('registros')

class RastreamentoBusca(View):
    template_name = "rastreamentoBusca.html"
    def get(self, request):
        context = {}
        context['pedidos'] = Pedido.objects.all()
        return render(request, self.template_name, context)

    def post(self, request):
        context = {}
        context['pedidos'] = Pedido.objects.filter(identificacao__startswith=request.POST.get('identificacao'),
                                                    registro__data=request.POST.get('dataRegistro'))
                                                    #UFDestino=request.POST.get('UFDestino'))
                                                    #transportadora__nome=request.POST.get('transportadora'),
                                                    #dataPrevista=request.POST.get('dataPrevista'),
                                                    #status=request.POST.get('status'))
        return render(request, self.template_name, context)

class RastreamentoPeriodo(View):
    template_name = "rastreamentoPeriodo.html"
    def get(self, request):
        context = {}
        context['pedidos'] = Pedido.objects.all()
        return render(request, self.template_name, context)

    def post(self, request):
        context = {}
        context['pedidos'] = Pedido.objects.filter(registro__data__range=(request.POST.get('dataInicio'), request.POST.get('dataFim')))
        return render(request, self.template_name, context)

#class ListaProgramacaoTransporte(ListView):
#     model = ProgramacaoTransporte

# class VerProgramacaoTransporte(DetailView):
#     model = ProgramacaoTransporte
class CriarProgramacaoTransporte(CreateView):
    template_name = "listar_programacao.html"
    def get(self, request):
        context = {}
        context['programacoes'] = ProgramacaoTransporte.objects.all()
        transportadoras = []
        for transportadora in Transportadora.objects.all():
            if ProgramacaoTransporte.objects.filter(transportadora=transportadora).exists():
                transportadoras.append(transportadora)
        context['transportadoras'] = transportadoras
        for transportadora in transportadoras:
            performance = calcula_performance(Pedido.objects.filter(transportadora=transportadora))
            transportadora.performance = performance
        pedidos = Pedido.objects.all()
        performance = calcula_performance(pedidos)
        context['performance'] = performance
        custoTotal = 0
        programacoes = ProgramacaoTransporte.objects.all()
        for programacao in programacoes:
            custoTotal += programacao.precoEstimado
        context['custoTotal'] = custoTotal
        tempoTotal = 0
        for programacao in programacoes:
            tempoTotal += programacao.prazoEstimado 
        context['tempoTotal'] = tempoTotal
        for registro in Registro.objects.all():
            DistribuiPedidos(registro)
        return render(request, self.template_name, context)

    def post(self, request):
        transportadoras = []
        for transportadora in Transportadora.objects.all():
            if ProgramacaoTransporte.objects.filter(transportadora=transportadora).exists():
                transportadoras.append(transportadora)
        context['programacoes'] = ProgramacaoTransporte.objects.all()
        context['transportadoras'] = transportadoras
        return render(request, self.template_name, context)
    

class ListaProgramacaoTransporte(CreateView):
    template_name = "listar_programacao.html"
    def get(self, request):
        context = {}
        programacoes = ProgramacaoTransporte.objects.all()
        transportadoras = []
        for transportadora in Transportadora.objects.all():
            if ProgramacaoTransporte.objects.filter(transportadora=transportadora).exists():
                transportadoras.append(transportadora)
        context['programacoes'] = ProgramacaoTransporte.objects.all()
        context['transportadoras'] = transportadoras
        pedidos = Pedido.objects.all()
        for transportadora in transportadoras:
            performance = calcula_performance(Pedido.objects.filter(transportadora=transportadora))
            transportadora.performance = performance
        performance = calcula_performance(pedidos)
        context['performance'] = performance
        custoTotal = 0
        for programacao in programacoes:
            custoTotal += programacao.precoEstimado
        context['custoTotal'] = custoTotal
        tempoTotal = 0
        for programacao in programacoes:
            tempoTotal += programacao.prazoEstimado 
        context['tempoTotal'] = tempoTotal

        return render(request, self.template_name, context)

    def post(self, request):
        return render(request, self.template_name, context)

class ProgramarRegistro(CreateView):
    def get(self, request, pk):
        registro = Registro.objects.get(pk=pk)
        pedidos_sem_transportadora = DistribuiPedidos(registro)

        print("Pedidos sem transportadora:")
        for pedido in pedidos_sem_transportadora:
            print(pedido.identificacao)

        return redirect("/programacao")
    def post(self, request, pk):
        return redirect("/programacao")

def criar_programacao(request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="ProgramaçãoDeTransporte.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Programacoes')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Pedido', 'Registro', 'Transportadora', 'Data',]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = ProgramacaoTransporte.objects.all().values_list('pedido', 'registro', 'transportadora', 'data')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response    

# class AlteraProgramacaoTransporte(UpdateView):
#     model = ProgramacaoTransporte
#     fields = ['pedido', 'registro', 'transportadora', 'data']
#     success_url = reverse_lazy('lista_programacao')

# class DeletaProgramacaoTransporte(DeleteView):
#     model = ProgramacaoTransporte
#     success_url = reverse_lazy('lista_programacao') 

def ImportarNotFis(request):
    file = [ linha.decode("utf-8", "replace") for linha in request.FILES['arquivo'].readlines()]

    remetente, destinatario, data, hora = file[0][3:38], file[0][38:73], file[0][73:79], file[0][79:83]
    cep_embarcadora, data_embarque = file[2][107:116], file[2][125:133]

    registro = Registro.objects.create(arquivo = request.FILES['arquivo'])

    file = file[3:]
    for i in range(len(file)):
        if file[i][:3] == "312":
            nome_destinatario = file[i][3:43]
            cpf_destinatario = file[i][39:43]
            cep_destinatario = file[i][167:176]

            codigo = file[i+1][32:40]
            peso = float(file[i+1][100:105]) + int(file[i+1][105:107])*0.01
            valor = float(file[i+1][85:98]) + int(file[i+1][98:100])*0.01

            UFDestino = DeterminaEstado(cep_destinatario)
            pedido = Pedido(
                identificacao = nome_destinatario,
                codigo = codigo,
                valor = valor,
                peso = peso,
                origem = cep_embarcadora,
                destino = cep_destinatario,
                registro = registro,
                UFDestino= UFDestino)
            pedido.save()
    return registro.pk


def ImportarRegistroExcel(request):
    tabela_registro = pandas.read_excel(request.FILES['arquivo'])
    registro = Registro.objects.create(arquivo = request.FILES['arquivo'])

    for i in range(len(tabela_registro)):
        row = tabela_registro.iloc[i]
        pedido = Pedido(
                codigo = row[0],
                identificacao = row[1],
                valor = row[4],
                peso = row[5],
                origem = row[2],
                destino = row[3],
                registro = registro
            )
        pedido.save()
    return registro.pk

def DownloadExcelPadrao(request):
    file_path = os.path.join("core/static/media/RegistroBase/RegistroBase.xlsx")
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def DownloadTabelaPrazoPadrao(request):
    file_path = os.path.join("core/static/media/TabelaPrazo/tabelaPrazos.xlsx")
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def DownloadTabelaPrecoPadrao(request):
    file_path = os.path.join("core/static/media/TabelaPreco/tabelaPreco.xlsx")
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def BuscaTransportadoras(pedido):
    pedido_origem_CEP = int(pedido.origem)
    pedido_destino_CEP = int(pedido.destino)
    pedido_peso = float(pedido.peso)

    path_localizacao = os.path.abspath('core/static/media/TabelaPrazo/tabelaPrazos.xlsx')
    tabela_localizacao = pandas.read_excel(path_localizacao, sheet_name='Planilha1')
    lista_inicioCEP = tabela_localizacao['CEP INICIAL']
    lista_fimCEP = tabela_localizacao['CEP FINAL']
    lista_UF = tabela_localizacao['UF']
    lista_regiao = tabela_localizacao['REGIÃO']

    for i in range(len(lista_inicioCEP)):
        inicio = int(lista_inicioCEP[i].replace("-", ""))
        fim = int(lista_fimCEP[i].replace("-", ""))

        if pedido_origem_CEP >= inicio and pedido_origem_CEP <= fim:
            pedido_origem_UF = lista_UF[i]
            pedido_origem_regiao = lista_regiao[i]

        # if pedido_destino_CEP >= inicio and pedido_destino_CEP <= fim:
        #     pedido_destino_UF = lista_UF[i]
        #     pedido_destino_regiao = lista_regiao[i]


    transportadoras = Transportadora.objects.all()
    transportadoras_match = []
    for transportadora in transportadoras:
        match_destino, match_origem = False, False
        # path_prazo = {PLANILHA DE PRAZOS DA TRANSPORTADORA SELECIONADA}
        path_prazo = os.path.abspath('core/static/media/TabelaPrazo/tabelaPrazos.xlsx')
        tabela_prazos = pandas.read_excel(path_localizacao, sheet_name='Planilha1')
        lista_transportadora_inicioCEP = tabela_prazos['CEP INICIAL']
        lista_transportadora_fimCEP = tabela_prazos['CEP FINAL']
        lista_transportadora_UF = tabela_prazos['UF']
        lista_transportadora_regiao = tabela_prazos['REGIÃO']
        #Depende da tabela de prazos da transportadora, por enquanto, vou deixar o prazo do sedex da tabela do correio como default
        lista_transportadora_prazo = tabela_prazos['Prazo Sedex']
        for i in range(len(lista_transportadora_inicioCEP)):
                inicio = int(lista_transportadora_inicioCEP[i].replace("-", ""))
                fim = int(lista_transportadora_fimCEP[i].replace("-", ""))
                if pedido_destino_CEP >= inicio and pedido_destino_CEP <= fim:
                    match_destino = True
                    transportadora_prazo = int(lista_transportadora_prazo[i])
                    pedido_destino_UF = lista_UF[i]
                    pedido_destino_regiao = lista_regiao[i]
        if match_destino:
            #path_preco = {PLANILHA DE PREÇOS DA TRANSPORTADORA SELECIONADA}
            path_preco = os.path.abspath('core/static/media/TabelaPreco/tabelaPreco.xlsx')
            lista_planilhas_preco = pandas.ExcelFile(path_preco).sheet_names
            for sede_transportadora in lista_planilhas_preco:
                transportadora_origem_UF = sede_transportadora
                if transportadora_origem_UF == pedido_origem_UF:
                    match_origem = True
                    transportadora.preco = DeterminaPreco(path_preco, sede_transportadora, pedido_origem_regiao, pedido_destino_UF, pedido_destino_regiao, pedido_peso, pedido, transportadora)
            if match_origem:
                transportadoras_match.append(transportadora)
                transportadora.save()

    if pedido_destino_regiao == "METROPOLITANA":
        pedido_destino_regiao = "C"
    elif pedido_destino_regiao == "INTERIOR":
        pedido_destino_regiao = "I"

    transportadoras_ranqueadas = Ranquear(pedido, transportadoras_match, pedido_destino_UF, pedido_destino_regiao)

    return transportadoras_ranqueadas

def DeterminaPreco(path_preco, sede_transportadora, regiao_origem, uf_destino, regiao_destino, peso, pedido, transportadora):
    tabela_preco = pandas.read_excel(path_preco, sheet_name = sede_transportadora)

    regiao_origem2 = "METROPOLITANA"
    regiao_destino2 = "METROPOLITANA"
    
    if regiao_origem2 == "METROPOLITANA":
        if regiao_destino2 == "METROPOLITANA":
            if uf_destino == "AC":
                precos = tabela_preco.loc[1:17, 'Estado']
            elif uf_destino == "AL":
                precos = tabela_preco.loc[1:17, 'Unnamed: 2']
            elif uf_destino == "AP":
                precos = tabela_preco.loc[1:17, 'Unnamed: 3']
            elif uf_destino == "AM":
                precos = tabela_preco.loc[1:17, 'Unnamed: 4']
            elif uf_destino == "BA":
                precos = tabela_preco.loc[1:17, 'Unnamed: 5']
            elif uf_destino == "CE":
                precos = tabela_preco.loc[1:17, 'Unnamed: 6']
            elif uf_destino == "DF":
                precos = tabela_preco.loc[1:17, 'Unnamed: 7']
            elif uf_destino == "ES":
                precos = tabela_preco.loc[1:17, 'Unnamed: 8']
            elif uf_destino == "GO":
                precos = tabela_preco.loc[1:17, 'Unnamed: 9']
            elif uf_destino == "MA":
                precos = tabela_preco.loc[1:17, 'Unnamed: 10']
            elif uf_destino == "MT":
                precos = tabela_preco.loc[1:17, 'Unnamed: 11']
            elif uf_destino == "MS":
                precos = tabela_preco.loc[1:17, 'Unnamed: 12']
            elif uf_destino == "MG":
                precos = tabela_preco.loc[1:17, 'Unnamed: 13']
            elif uf_destino == "PA":
                precos = tabela_preco.loc[1:17, 'Unnamed: 14']
            elif uf_destino == "PB":
                precos = tabela_preco.loc[1:17, 'Unnamed: 15']
            elif uf_destino == "PR":
                precos = tabela_preco.loc[1:17, 'Unnamed: 16']
            elif uf_destino == "PE":
                precos = tabela_preco.loc[1:17, 'Unnamed: 17']
            elif uf_destino == "PI":
                precos = tabela_preco.loc[1:17, 'Unnamed: 18']
            elif uf_destino == "RJ":
                precos = tabela_preco.loc[1:17, 'Unnamed: 19']
            elif uf_destino == "RN":
                precos = tabela_preco.loc[1:17, 'Unnamed: 20']
            elif uf_destino == "RS":
                precos = tabela_preco.loc[1:17, 'Unnamed: 21']
            elif uf_destino == "RO":
                precos = tabela_preco.loc[1:17, 'Unnamed: 22']
            elif uf_destino == "RR":
                precos = tabela_preco.loc[1:17, 'Unnamed: 23']
            elif uf_destino == "SC":
                precos = tabela_preco.loc[1:17, 'Unnamed: 24']
            elif uf_destino == "SP":
                precos = tabela_preco.loc[1:17, 'Unnamed: 25']
            elif uf_destino == "SE":
                precos = tabela_preco.loc[1:17, 'Unnamed: 26']
            elif uf_destino == "TO":
                precos = tabela_preco.loc[1:17, 'Unnamed: 27']
        elif regiao_destino == "INTERIOR":
            if uf_destino == "AC":
                precos = tabela_preco.loc[20:36, 'Estado']
            elif uf_destino == "AL":
                precos = tabela_preco.loc[20:36, 'Unnamed: 2']
            elif uf_destino == "AP":
                precos = tabela_preco.loc[20:36, 'Unnamed: 3']
            elif uf_destino == "AM":
                precos = tabela_preco.loc[20:36, 'Unnamed: 4']
            elif uf_destino == "BA":
                precos = tabela_preco.loc[20:36, 'Unnamed: 5']
            elif uf_destino == "CE":
                precos = tabela_preco.loc[20:36, 'Unnamed: 6']
            elif uf_destino == "DF":
                precos = tabela_preco.loc[20:36, 'Unnamed: 7']
            elif uf_destino == "ES":
                precos = tabela_preco.loc[20:36, 'Unnamed: 8']
            elif uf_destino == "GO":
                precos = tabela_preco.loc[20:36, 'Unnamed: 9']
            elif uf_destino == "MA":
                precos = tabela_preco.loc[20:36, 'Unnamed: 10']
            elif uf_destino == "MT":
                precos = tabela_preco.loc[20:36, 'Unnamed: 11']
            elif uf_destino == "MS":
                precos = tabela_preco.loc[20:36, 'Unnamed: 12']
            elif uf_destino == "MG":
                precos = tabela_preco.loc[20:36, 'Unnamed: 13']
            elif uf_destino == "PA":
                precos = tabela_preco.loc[20:36, 'Unnamed: 14']
            elif uf_destino == "PB":
                precos = tabela_preco.loc[20:36, 'Unnamed: 15']
            elif uf_destino == "PR":
                precos = tabela_preco.loc[20:36, 'Unnamed: 16']
            elif uf_destino == "PE":
                precos = tabela_preco.loc[20:36, 'Unnamed: 17']
            elif uf_destino == "PI":
                precos = tabela_preco.loc[20:36, 'Unnamed: 18']
            elif uf_destino == "RJ":
                precos = tabela_preco.loc[20:36, 'Unnamed: 19']
            elif uf_destino == "RN":
                precos = tabela_preco.loc[20:36, 'Unnamed: 20']
            elif uf_destino == "RS":
                precos = tabela_preco.loc[20:36, 'Unnamed: 21']
            elif uf_destino == "RO":
                precos = tabela_preco.loc[20:36, 'Unnamed: 22']
            elif uf_destino == "RR":
                precos = tabela_preco.loc[20:36, 'Unnamed: 23']
            elif uf_destino == "SC":
                precos = tabela_preco.loc[20:36, 'Unnamed: 24']
            elif uf_destino == "SP":
                precos = tabela_preco.loc[20:36, 'Unnamed: 25']
            elif uf_destino == "SE":
                precos = tabela_preco.loc[20:36, 'Unnamed: 26']
            elif uf_destino == "TO":
                precos = tabela_preco.loc[20:36, 'Unnamed: 27']
    elif regiao_origem == "INTERIOR":
        if regiao_destino == "METROPOLITANA":
            if uf_destino == "AC":
                precos = tabela_preco.loc[39:55, 'Estado']
            elif uf_destino == "AL":
                precos = tabela_preco.loc[39:55, 'Unnamed: 2']
            elif uf_destino == "AP":
                precos = tabela_preco.loc[39:55, 'Unnamed: 3']
            elif uf_destino == "AM":
                precos = tabela_preco.loc[39:55, 'Unnamed: 4']
            elif uf_destino == "BA":
                precos = tabela_preco.loc[39:55, 'Unnamed: 5']
            elif uf_destino == "CE":
                precos = tabela_preco.loc[39:55, 'Unnamed: 6']
            elif uf_destino == "DF":
                precos = tabela_preco.loc[39:55, 'Unnamed: 7']
            elif uf_destino == "ES":
                precos = tabela_preco.loc[39:55, 'Unnamed: 8']
            elif uf_destino == "GO":
                precos = tabela_preco.loc[39:55, 'Unnamed: 9']
            elif uf_destino == "MA":
                precos = tabela_preco.loc[39:55, 'Unnamed: 10']
            elif uf_destino == "MT":
                precos = tabela_preco.loc[39:55, 'Unnamed: 11']
            elif uf_destino == "MS":
                precos = tabela_preco.loc[39:55, 'Unnamed: 12']
            elif uf_destino == "MG":
                precos = tabela_preco.loc[39:55, 'Unnamed: 13']
            elif uf_destino == "PA":
                precos = tabela_preco.loc[39:55, 'Unnamed: 14']
            elif uf_destino == "PB":
                precos = tabela_preco.loc[39:55, 'Unnamed: 15']
            elif uf_destino == "PR":
                precos = tabela_preco.loc[39:55, 'Unnamed: 16']
            elif uf_destino == "PE":
                precos = tabela_preco.loc[39:55, 'Unnamed: 17']
            elif uf_destino == "PI":
                precos = tabela_preco.loc[39:55, 'Unnamed: 18']
            elif uf_destino == "RJ":
                precos = tabela_preco.loc[39:55, 'Unnamed: 19']
            elif uf_destino == "RN":
                precos = tabela_preco.loc[39:55, 'Unnamed: 20']
            elif uf_destino == "RS":
                precos = tabela_preco.loc[39:55, 'Unnamed: 21']
            elif uf_destino == "RO":
                precos = tabela_preco.loc[39:55, 'Unnamed: 22']
            elif uf_destino == "RR":
                precos = tabela_preco.loc[39:55, 'Unnamed: 23']
            elif uf_destino == "SC":
                precos = tabela_preco.loc[39:55, 'Unnamed: 24']
            elif uf_destino == "SP":
                precos = tabela_preco.loc[39:55, 'Unnamed: 25']
            elif uf_destino == "SE":
                precos = tabela_preco.loc[39:55, 'Unnamed: 26']
            elif uf_destino == "TO":
                precos = tabela_preco.loc[39:55, 'Unnamed: 27']
        elif regiao_destino == "INTERIOR":
            if uf_destino == "AC":
                precos = tabela_preco.loc[58:74, 'Estado']
            elif uf_destino == "AL":
                precos = tabela_preco.loc[58:74, 'Unnamed: 2']
            elif uf_destino == "AP":
                precos = tabela_preco.loc[58:74, 'Unnamed: 3']
            elif uf_destino == "AM":
                precos = tabela_preco.loc[58:74, 'Unnamed: 4']
            elif uf_destino == "BA":
                precos = tabela_preco.loc[58:74, 'Unnamed: 5']
            elif uf_destino == "CE":
                precos = tabela_preco.loc[58:74, 'Unnamed: 6']
            elif uf_destino == "DF":
                precos = tabela_preco.loc[58:74, 'Unnamed: 7']
            elif uf_destino == "ES":
                precos = tabela_preco.loc[58:74, 'Unnamed: 8']
            elif uf_destino == "GO":
                precos = tabela_preco.loc[58:74, 'Unnamed: 9']
            elif uf_destino == "MA":
                precos = tabela_preco.loc[58:74, 'Unnamed: 10']
            elif uf_destino == "MT":
                precos = tabela_preco.loc[58:74, 'Unnamed: 11']
            elif uf_destino == "MS":
                precos = tabela_preco.loc[58:74, 'Unnamed: 12']
            elif uf_destino == "MG":
                precos = tabela_preco.loc[58:74, 'Unnamed: 13']
            elif uf_destino == "PA":
                precos = tabela_preco.loc[58:74, 'Unnamed: 14']
            elif uf_destino == "PB":
                precos = tabela_preco.loc[58:74, 'Unnamed: 15']
            elif uf_destino == "PR":
                precos = tabela_preco.loc[58:74, 'Unnamed: 16']
            elif uf_destino == "PE":
                precos = tabela_preco.loc[58:74, 'Unnamed: 17']
            elif uf_destino == "PI":
                precos = tabela_preco.loc[58:74, 'Unnamed: 18']
            elif uf_destino == "RJ":
                precos = tabela_preco.loc[58:74, 'Unnamed: 19']
            elif uf_destino == "RN":
                precos = tabela_preco.loc[58:74, 'Unnamed: 20']
            elif uf_destino == "RS":
                precos = tabela_preco.loc[58:74, 'Unnamed: 21']
            elif uf_destino == "RO":
                precos = tabela_preco.loc[58:74, 'Unnamed: 22']
            elif uf_destino == "RR":
                precos = tabela_preco.loc[58:74, 'Unnamed: 23']
            elif uf_destino == "SC":
                precos = tabela_preco.loc[58:74, 'Unnamed: 24']
            elif uf_destino == "SP":
                precos = tabela_preco.loc[58:74, 'Unnamed: 25']
            elif uf_destino == "SE":
                precos = tabela_preco.loc[58:74, 'Unnamed: 26']
            elif uf_destino == "TO":
                precos = tabela_preco.loc[58:74, 'Unnamed: 27']

    lista_precos = [preco for preco in precos]
    if peso >= 0 and peso <= 0.3:
        preco = lista_precos[0] 
    elif peso > 0.3 and peso <= 0.5:
        preco = lista_precos[1] 
    elif peso > 0.5 and peso <= 1:
        preco = lista_precos[2] 
    elif peso > 1 and peso <= 1.5:
        preco = lista_precos[3] 
    elif peso > 1.5 and peso <= 2:
        preco = lista_precos[4] 
    elif peso > 2 and peso <= 2.5:
        preco = lista_precos[5] 
    elif peso > 2.5 and peso <= 3:
        preco = lista_precos[6] 
    elif peso > 3 and peso <= 3.5:
        preco = lista_precos[7] 
    elif peso > 3.5 and peso <= 4:
        preco = lista_precos[8] 
    elif peso > 4 and peso <= 4.5:
        preco = lista_precos[9] 
    elif peso > 4.5 and peso <= 5:
        preco = lista_precos[10] 
    elif peso > 5 and peso <= 6:
        preco = lista_precos[11] 
    elif peso > 6 and peso <= 7:
        preco = lista_precos[12] 
    elif peso > 7 and peso <= 8:
        preco = lista_precos[13] 
    elif peso > 8 and peso <= 9:
        preco = lista_precos[14] 
    elif peso > 9 and peso <= 10:
        preco = lista_precos[15] 
    elif peso > 10:
        preco = lista_precos[15] + lista_precos[16]*round((peso - 10) + 0.5) 

    preco = preco + (pedido.valor * transportadora.adValorem)
    
    return preco


def Ranquear(pedido, transportadoras, UFDestino, regiaoDestino):
    regraDeNegocio = RegraDeNegocio.objects.get(UF="SP", regiao="C")
    
    for transportadora in transportadoras:
        #DELETAR DEPOIS QUE AS TRANSPORTADORAS TIVEREM TABELAS SEPARADAS
        if transportadora.id == 1:
            transportadora.preco = 12
            transportadora_prazo = 9
        elif transportadora.id == 6:
            transportadora.preco = 20
            transportadora_prazo = 12
    prazos = Prazo.objects.all()
    min_prazo = min(prazos,key=attrgetter('prazoSEDEX')).prazoSEDEX
    min_preco = min(transportadoras,key=attrgetter('preco')).preco
    min_performance = min(transportadoras,key=attrgetter('performance')).performance
    max_prazo = max(prazos,key=attrgetter('prazoSEDEX')).prazoSEDEX
    max_preco = max(transportadoras,key=attrgetter('preco')).preco
    max_performance = max(transportadoras,key=attrgetter('performance')).performance
    range_prazo = max_prazo - min_prazo
    range_preco = max_preco - min_preco
    range_performance = max_performance - min_performance

    for transportadora in transportadoras:
        if range_prazo != 0:
            transportadora.rankingPrazo = (10 - min_prazo)/range_prazo
        else:
            transportadora.rankingPrazo = 0
        if range_preco != 0:
            transportadora.rankingPreco = (transportadora.preco - min_preco)/range_preco
        else: transportadora.rankingPreco = 0
        if range_performance != 0:
            transportadora.rankingPerformance = 1 - ((transportadora.performance - min_performance)/range_performance)
        else:
            transportadora.rankingPerformance = 0
        transportadora.rankingGeral = (transportadora.rankingPrazo * regraDeNegocio.prazo) + (transportadora.rankingPreco * regraDeNegocio.preco) + (transportadora.rankingPerformance * regraDeNegocio.performance)
        transportadora.save()

    transportadoras.sort(key=lambda x: x.rankingGeral)

    return transportadoras

def DistribuiPedidos(registro):
    pedidos = Pedido.objects.select_related().filter(registro = registro)
    pedidos_sem_transportadora = []

    for pedido in pedidos:
        pedido_alocado = False
        transportadoras = BuscaTransportadoras(pedido)
        for transportadora in transportadoras:
            transportadora.rankingPrazo, transportadora.rankingPreco, transportadora.rankingPerformance, transportadora.rankingGeral = 0, 0, 0, 0
            if transportadora.quantidadeAtual < transportadora.maximoPedidos and transportadora.valorAtual < transportadora.valorMaximo:
                prazo = Prazo.objects.filter(transportadora=transportadora)[0]
                preco = Valor.objects.filter(transportadora=transportadora)[0]
                programacao = ProgramacaoTransporte(
                        pedido = pedido,
                        registro = registro,
                        transportadora = transportadora,
                        prazoEstimado =  prazo.prazoSEDEX,
                        precoEstimado = preco.valor
                    )
                programacao.save()
                pedido.transportadora = transportadora
                pedido.save()
                transportadora.quantidadeAtual += 1
                transportadora.valorAtual += pedido.valor
                transportadora.preco, transportadora_prazo = 0, 0
                transportadora.save()

                pedido_alocado = True
                break
        if not pedido_alocado:
            pedidos_sem_transportadora.append(pedido)

    for transportadora in Transportadora.objects.all():
        transportadora.quantidadeAtual, transportadora.valorAtual = 0, 0
        transportadora.save()

    return pedidos_sem_transportadora


class TransportadoraOCOREN(View):
    def get(self, request, *args, **kwargs):
        arquivos = RastreamentoArquivo.objects.all()
        context = {}
        context['arquivos'] = arquivos
        return render(request, 'transportadora_OCOREN.html', context)
    def post(self, request, *args, **kwargs):
        form = RastreamentoForm(request.POST, request.FILES)
        if form.is_valid():
            #ImportarNotFis(request)
            ImportarRastreamento(request)
        arquivos = RastreamentoArquivo.objects.all()
        context = {
            'form': form,
            'arquivos':arquivos
        }

        return render(request, 'transportadora_OCOREN.html', context)

def ImportarRastreamento(request):
    file = [ linha.decode("utf-8", "replace") for linha in request.FILES['arquivo'].readlines()]

    file = file[3:]
    for i in range(len(file)):
        if file[i][:3] == "342":
            tipo = 'O'
            codigo = file[i][20:28]
            ocorrencia = file[i][28:30]
            data = file[i][30:38]

            if ocorrencia == '01' or ocorrencia == '02':
                status = 'F'
            else:
                status = 'X'

            for pedido in Pedido.objects.all() :
                if codigo == pedido.codigo:
                    pedido_encontrado = True
                    pedido_relacionado = pedido
                    pedido_relacionado.status = status
                    pedido_relacionado.save()
                    break
                else:
                    pedido_encontrado = False

            if pedido_encontrado:
                rastreamento = RastreamentoArquivo(
                        data = data,
                        tipo = tipo,
                        codigo = codigo,
                        pedido = pedido_relacionado,
                        status = status,
                        arquivo = request.FILES['arquivo']
                    )
                rastreamento.save()

        if file[i][:3] == "322":
            pass
                    # tipo = 'O'
                    # codigo = file[i][20:28]
                    # ocorrencia = file[i][28:30]
                    # data = file[i][30:38]

                    # if ocorrencia == '01' or ocorrencia == '02':
                    #     status = 'F'
                    # else:
                    #     status = 'X'

                    # for pedido in Pedido.objects.all() :
                    #     if codigo == pedido.codigo:
                    #         pedido_encontrado = True
                    #         pedido_relacionado = pedido
                    #         pedido_relacionado.status = status
                    #         pedido_relacionado.save()
                    #         break
                    #     else:
                    #         pedido_encontrado = False

                    # if pedido_encontrado:
                    #     rastreamento = RastreamentoArquivo(
                    #             data = data,
                    #             tipo = tipo,
                    #             codigo = codigo,
                    #             pedido = pedido_relacionado,
                    #             status = status,
                    #             arquivo = request.FILES['arquivo']
                    #         )
                    #     rastreamento.save()

# def BuscarPrecos(pedido):
#     origem = DeterminaRegiao(pedido.origem)
#     destino = DeterminaRegiao(pedido.destino)

#     transportadoras = []
#     for transportadora in Transportadora.objects.all():
#         if origem in transportadora.regiao and destino in transportadora.regiao:
#             transportadoras.append(transportadora)


#     UFDestino, regiaoDestino = pedido.UFDestino, pedido.regiaoDestino
#     regiaoOrigem = "C"

#     tabelas = []
#     if regiaoOrigem == "C" and regiaoDestino == "C":
#         for transportadora in transportadoras:
#             tabela = Tabela_Capital_Capital.objects.filter(transportadora = transportadora, estado = UFDestino)[0]
#             tabelas.append(tabela)
#     if regiaoOrigem == "C" and regiaoDestino == "I":
#         for transportadora in transportadoras:
#             tabela = Tabela_Capital_Interior.objects.filter(transportadora = transportadora, estado = UFDestino)[0]
#             tabelas.append(tabela)
#     if regiaoOrigem == "I" and regiaoDestino == "C":
#         for transportadora in transportadoras:
#             tabela = Tabela_Interior_Capital.objects.filter(transportadora = transportadora, estado = UFDestino)[0]
#             tabelas.append(tabela)
#     if regiaoOrigem == "I" and regiaoDestino == "I":
#         for transportadora in transportadoras:
#             tabela = Tabela_Interior_Interior.objects.filter(transportadora = transportadora, estado = UFDestino)[0]
#             tabelas.append(tabela)
            
#     tabelas = sorted(tabelas, key=lambda x: int(x.valor))

#     return tabelas

# def DeterminaRegiao(cep):
#     cep = int(cep)

#     if cep >= 1000000 and cep <= 39999999:
#         regiao = "SUDESTE"
#     elif cep >= 40000000 and cep <= 65999999:
#         regiao = "NORDESTE"
#     elif cep >= 66000000 and cep <= 69999999:
#         regiao = "NORTE"
#     elif cep >= 76800000 and cep <= 77999999:
#         regiao = "NORTE"
#     elif cep >= 70000000 and cep <= 76799999:
#         regiao = "CENTROOESTE"
#     elif cep >= 78000000 and cep <= 79999999:
#         regiao = "CENTROOESTE"
#     elif cep >= 80000000 and cep <= 99999999:
#         regiao = "SUL"
#     else:
#         regiao = "ERRO"

#     return regiao


"""Implementação do algoritmo de performance"""


def calcula_performance(pedidos):
    """Calcula a performance da transportadora em porcentagem.
    
    Soma cada fração de prazo/prazo_efetivo de cada pedido
    e divide essa soma pelo numero de pedidos

    Args:
        lista de pedidos
    Returns:
        porcentagem de 0 a 100%
    """
    soma = 0
    for pedido in pedidos:
        data_ocoren = pedido.data_ocoren
        data_conemb = pedido.data_conemb
        prazo_efetivo = _calcula_prazo_efetivo(data_ocoren, data_conemb)

        frac = pedido.prazo / (prazo_efetivo.days +1)
        soma += frac
    performance = soma / len(pedidos) *100
    if performance > 100:
        performance = 100
    elif performance <= 0:
        performance = 0
    return performance


def _calcula_prazo_efetivo(data_ocoren, data_conemb):
    """Calcula prazo efetivo
    
    Args:
        data_ocoren: objeto do tipo date ou datetime
        data_conemb: objeto do tipo date ou datetime
    
    Returns:
        objeto do tipo timedelta correspondente ao prazo
    """
    return data_ocoren - data_conemb

def leTabelaPrazo(transportadora_pk):
    transportadora = Transportadora.objects.get(pk=transportadora_pk)
    transportadora_pk = transportadora.pk
    path = os.path.abspath('core/static/media/TabelaPrazo/tabelaPrazos.xlsx')
    tabela = pandas.read_excel(path, sheet_name='Planilha1')
    nome = tabela['Localidade']
    UF = tabela['UF']
    inicioCEP = tabela['CEP INICIAL'].replace("-","")
    fimCEP = tabela['CEP FINAL'].replace("-","")
    prazoSEDEX = tabela['Prazo Sedex']
    prazoPAC = tabela['Prazo PAC']
    regiao = tabela['REGIÃO']

    i = 0
    while (nome[i] != None):
        if regiao[i] == "METROPOLITANA" or regiao[i] == "CAPITAL":
            regiao[i] = 'C'
        else:
            regiao[i] = 'I'
        prazo = Prazo.objects.create(nome = nome[i], UF = UF[i], inicioCEP = inicioCEP[i], fimCEP = fimCEP[i], prazoSEDEX = prazoSEDEX[i], prazoPAC = prazoPAC[i], regiao = regiao[i], transportadora=transportadora)
        prazo.save()
        i += 1
        

class RelatorioFinanceiro (View):
    template_name = 'criar_relatorio_financeiro.html'
    def get (self,request, tipo_de_relatorio):
        return render(request, template_name)

#funcao para escrever os dados de rastreamento num arquivo .xlsx
def exportar_rastreamento_views(request):
    if request.method == 'POST':
        campos = ['Cliente', 'Valor', 'Data de Registro', 'UF de Origem', 'UF de Destino', 'Transportadora']

        tamanho = request.POST.get('tamanho')

        filename =  apps.get_app_config('core').path + '/static/media/Exportacao/rastreamento.xlsx' 
        print(filename)
        workbook = xlsxwriter.Workbook(filename)
        ws = workbook.add_worksheet()

        for j in range(len(campos)):
            ws.write(0, j, campos[j])

        row = 2
        for i in range(int(tamanho)):
            dado = request.POST.get('input' + str(i))
            ws.write(row, i % len(campos), dado)

            if i % len(campos) == 5:
                row += 1

        workbook.close()
    return HttpResponse('Feito')


#view para relatorio de performance
class GerarRelatorioPerformance(View):
    def get(self, request, tipo_de_relatorio):
        context = {}

        if tipo_de_relatorio == 'ranking':
            now = datetime.datetime.now()
            data_gerado = str(now.day) + '/' + str(now.month) + '/' + str(now.year) 

            transportadoras_por_performance = Transportadora.objects.order_by('performance')
            context['transportadora_list'] = []
            for i in range(0, len(transportadoras_por_performance)):
                context['transportadora_list'].append({
                        'ranking' : i + 1,
                        'transportadora' : transportadoras_por_performance[i]
                        })
            context['data_gerado'] = data_gerado 
    
            path_template = 'relatorio_performance_' + tipo_de_relatorio + '.html'
            template = get_template(path_template)
            html = template.render(context)
            options = {
                'page-size' : "Letter",
                'encoding' : "UTF-8"
                   }
            file_css = apps.get_app_config('core').path + '/static/css/relatorio.css'
            css = [file_css]
            pdf = pdfkit.from_string(html, False, css=css, options=options)
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="ranking_performance.pdf"'
            filename='relatorio.pdf'
    
            return response

        elif tipo_de_relatorio == 'estado':

            transportadoras = Transportadora.objects.all()
            context = {
                    'transportadora_list' : transportadoras
                    } 
            return render(request, 'criar_relatorio_performance.html', context)


    def post(self, request, tipo_de_relatorio):
        context = {} 

        if tipo_de_relatorio == 'estado':

            inicio_periodo = request.POST.get('inicio-periodo')
            fim_periodo = request.POST.get('fim-periodo')
            estado = request.POST.getlist('estado')
            transportadora_pks = request.POST.getlist('transportadora')

            #transformando string 'inicio-periodo' e 'fim-periodo' em datetime
            inicio = pandas.to_datetime(inicio_periodo).date()
            fim = pandas.to_datetime(fim_periodo).date()
            
            transportadoras = []
            estados = estado 
            #pegando objeto transportadora
            if 'ALL' in transportadora_pks:
                #filtrando pedidos 

                pedidos_filtrados = Pedido.objects.filter(
                        data_previsao__range=[inicio, fim],
                        UFDestino__in=estados
                        )
            else:
                for pk in transportadora_pks:
                    transportadoras.append(Transportadora.objects.get(pk=int(pk)))


                pedidos_filtrados = Pedido.objects.filter(
                        data_previsao__range=[inicio, fim],
                        UFDestino__in=estados,
                        transportadora__in=transportadoras,
                        )


            context['estado_list'] = []
            performance_estado = []
            pedidos_por_estado = []

            #algoritmo para calcular a media de performance por estado
            for estado in estados:
                pedidos_por_estado.append(pedidos_filtrados.filter(UFDestino=estado))

            for pedidos in pedidos_por_estado:
                performance_estado.append([pedido.transportadora.performance for pedido in pedidos])

            for i in range(0, len(estados)):
                if len(performance_estado[i]) > 0:
                    context['estado_list'].append({
                        'estado': estados[i],
                        'performance_media' : int(sum(performance_estado[i]) / len(performance_estado[i]))
                        })
                else:
                    context['estado_list'].append({
                        'estado': estados[i],
                        'performance_media' : 0
                        })
                    

            context['pedidos_list'] = pedidos_filtrados  
            inicio_periodo = str(inicio.day) + '/' + str(inicio.month) + '/' + str(inicio.year) 
            context['inicio_periodo'] = inicio_periodo

            fim_periodo = str(fim.day) + '/' + str(fim.month) + '/' + str(fim.year) 
            context['fim_periodo'] = fim_periodo

            context['transportadora_list'] = transportadoras

            path_template = 'relatorio_performance_' + tipo_de_relatorio + '.html'
            template = get_template(path_template)
            html = template.render(context)
            options = {
                'page-size' : "Letter",
                'encoding' : "UTF-8"
                    }
            file_css = apps.get_app_config('core').path + '/static/css/relatorio.css'
            css = [file_css]
            pdf = pdfkit.from_string(html, False, css=css, options=options)
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="relatorio_de_performance.pdf"'
            filename='relatorio.pdf'

            return response
            
#view para gerar relatorio de entrega
class GerarRelatorioEntrega(View):
    def get(self, request, tipo_de_relatorio):
        transportadoras = Transportadora.objects.all()
        context = {
                'transportadora_list' : transportadoras
                } 
        return render (request, 'criar_relatorio_entrega.html', context)


    def post(self, request, tipo_de_relatorio):
        context = {}
        #pegando infos do post request
        inicio_periodo = request.POST.get('inicio-periodo')
        fim_periodo = request.POST.get('fim-periodo')
        estado = request.POST.getlist('estado')
        transportadora_pks = request.POST.getlist('transportadora')
        tipo_de_relatorio = request.POST.get('tipo-de-relatorio')

        #transformando string 'inicio-periodo' e 'fim-periodo' em datetime
        inicio = pandas.to_datetime(inicio_periodo).date()
        fim = pandas.to_datetime(fim_periodo).date()

        transportadoras = []
        estados = estado 
        #pegando objeto transportadora
        if 'ALL' in transportadora_pks:
            #filtrando pedidos 

            pedidos_filtrados = Pedido.objects.filter(
                    data_previsao__range=[inicio, fim],
                    UFDestino__in=estados,
                    )
            
            transportadoras = Transportadora.objects.all()

        else:
            for pk in transportadora_pks:
                transportadoras.append(Transportadora.objects.get(pk=int(pk)))

            pedidos_filtrados = Pedido.objects.filter(
                    data_previsao__range=[inicio, fim],
                    UFDestino__in=estados,
                    transportadora__in=transportadoras,
                    )


        if tipo_de_relatorio == 'estado':
            context['estado_list'] = []
            for estado in estados:
                context['estado_list'].append({
                    'total' : pedidos_filtrados.filter(UFDestino=estado).count(),
                    'estado' : estado
                    }) 
        else:
            context['estado_list'] = estados



        if tipo_de_relatorio == 'transportadora':
            context['transportadora_list'] = []
            for transportadora in transportadoras:
                context['transportadora_list'].append({
                    'total' : pedidos_filtrados.filter(transportadora=transportadora).count(),
                    'transportadora' : transportadora
                    })
        else:
            context['transportadora_list'] = transportadoras

        if tipo_de_relatorio == 'periodo':
            context['total_de_pedidos'] = len(pedidos_filtrados)

        #context['pedidos_list'] = pedidos_filtrados  
        context['pedidos_list'] = []
        for pedido in pedidos_filtrados:
            try:
                preco = ProgramacaoTransporte.objects.get(pedido=pedido).precoEstimado
            except:
                preco = 'Não há programação de transporte'

            context['pedidos_list'].append({
                'pedido' : pedido,
                'frete' : preco
                })


        #testando uso de related_name para pegar o objeto ProgramacaoTransporte a partir do objeto Pedido (relacao de foreign key) 
        #pedido.programacao_transporte.get(pedido=pedido).precoEstimado

        inicio_periodo = str(inicio.day) + '/' + str(inicio.month) + '/' + str(inicio.year) 
        context['inicio_periodo'] = inicio_periodo

        fim_periodo = str(fim.day) + '/' + str(fim.month) + '/' + str(fim.year) 
        context['fim_periodo'] = fim_periodo

        path_template = 'relatorio_entrega_' + tipo_de_relatorio + '.html'
        template = get_template(path_template)
        html = template.render(context)
        options = {
            'page-size' : "Letter",
            'encoding' : "UTF-8"
                }
        file_css = apps.get_app_config('core').path + '/static/css/relatorio.css'
        css = [file_css]
        pdf = pdfkit.from_string(html, False, css=css, options=options)
        response = HttpResponse(pdf, content_type='application/pdf')

        response['Content-Disposition'] = 'attachment; filename="relatorio_de_entrega.pdf"'

        return response


class GerarGraficoEntrega(View):
    def get(self, request):
        transportadoras = Transportadora.objects.all()
        context = {
                'transportadora_list' : transportadoras
                } 
        return render(request, 'criar_grafico_entrega.html', context)

    
    def post(self, request):
        context = {}
        #pegando infos do post request
        inicio_periodo = request.POST.get('inicio-periodo')
        fim_periodo = request.POST.get('fim-periodo')
        estado = request.POST.getlist('estado')
        transportadora_pks = request.POST.getlist('transportadora')
        tipo_de_grafico = request.POST.get('tipo-de-grafico')

        #transformando string 'inicio-periodo' e 'fim-periodo' em datetime
        inicio = pandas.to_datetime(inicio_periodo).date()
        fim = pandas.to_datetime(fim_periodo).date()

        transportadoras = []
        estados = estado 
        #pegando objeto transportadora
        if 'ALL' in transportadora_pks:
            #filtrando pedidos 

            pedidos_filtrados = Pedido.objects.filter(
                    data_previsao__range=[inicio, fim],
                    UFDestino__in=estados,
                    )
            
            transportadoras = Transportadora.objects.all()

        else:
            for pk in transportadora_pks:
                transportadoras.append(Transportadora.objects.get(pk=int(pk)))

            pedidos_filtrados = Pedido.objects.filter(
                    data_previsao__range=[inicio, fim],
                    UFDestino__in=estados,
                    transportadora__in=transportadoras,
                    )

            context['estado_list'] = []
            for estado in estados:
                total_valor = 0
                pedidos_com_estado_em_questao = pedidos_filtrados.filter(UFDestino=estado).count()
                context['estado_list'].append({
                    'total' : pedidos_com_estado_em_questao,
                    'estado' : estado,
                    }) 


            datas_array = []
            data1 = inicio
            data2 = fim

            delta = data2 - data1


            for i in range(delta.days + 1):
                dia = data1 + datetime.timedelta(i)
                print(dia)
                datas_array.append(dia)

            datas_padrao=[]
            for data in datas_array:
                pedidos_do_dia = Pedido.objects.filter(data_previsao=data).count()
                data_em_questao = str(data.day) + '/' + str(data.month) + '/' + str(data.year)
                datas_padrao.append({
                    'data': data_em_questao,
                    'total': pedidos_do_dia,
                    })
            context['datas_e_valores'] = datas_padrao


            context['transportadora_list2'] = []
            
            for transportadora in transportadoras:
                pedidos_com_transportadora_em_questao = pedidos_filtrados.filter(transportadora=transportadora).count()
                context['transportadora_list2'].append({
                    'total' : pedidos_com_transportadora_em_questao,
                    'transportadora' : transportadora,
                    })


        inicio_periodo = str(inicio.day) + '/' + str(inicio.month) + '/' + str(inicio.year) 
        context['inicio_periodo'] = inicio_periodo

        fim_periodo = str(fim.day) + '/' + str(fim.month) + '/' + str(fim.year) 
        context['fim_periodo'] = fim_periodo

        path_template = 'graficos_entrega.html'
        return render(request, path_template, context)


class GerarGraficoPerformance(View):

    def get(self, request):
        transportadoras = Transportadora.objects.all()
        context = {
                'transportadora_list' : transportadoras
                } 
        return render(request, 'criar_grafico_performance.html', context)


    def post(self, request):

        # if 1==1:
        #     now = datetime.datetime.now()
        #     data_gerado = str(now.day) + '/' + str(now.month) + '/' + str(now.year) 

        #     transportadoras_por_performance = Transportadora.objects.order_by('performance')
        #     context['transportadora_ranking'] = []
        #     for i in range(0, len(transportadoras_por_performance)):
        #         context['transportadora_ranking'].append({
        #                 'ranking' : i + 1,
        #                 'transportadora' : transportadoras_por_performance[i]
        #                 })
        #     context['data_gerado'] = data_gerado  
            context = {} 
            inicio_periodo = request.POST.get('inicio-periodo')
            fim_periodo = request.POST.get('fim-periodo')
            estado = request.POST.getlist('estado')
            transportadora_pks = request.POST.getlist('transportadora')

            #transformando string 'inicio-periodo' e 'fim-periodo' em datetime
            inicio = pandas.to_datetime(inicio_periodo).date()
            fim = pandas.to_datetime(fim_periodo).date()
            
            transportadoras = []
            estados = estado 
            #pegando objeto transportadora
            if 'ALL' in transportadora_pks:
                #filtrando pedidos 

                pedidos_filtrados = Pedido.objects.filter(
                        data_previsao__range=[inicio, fim],
                        UFDestino__in=estados
                        )
                transportadoras = Transportadora.objects.all()
            else:
                for pk in transportadora_pks:
                    transportadoras.append(Transportadora.objects.get(pk=int(pk)))


                pedidos_filtrados = Pedido.objects.filter(
                        data_previsao__range=[inicio, fim],
                        UFDestino__in=estados,
                        transportadora__in=transportadoras,
                        )
            context['transportadora_performance']=[]
            for transportadora in transportadoras:
                context['transportadora_performance'].append({
                    'performance' : transportadora.performance,
                    'transportadora' : transportadora.nome,
                    }) 

            context['performance_media']=[]
            for estado in estados:
                pedidos_naquele_estado = Pedido.objects.filter(UFDestino=estado)
                soma_das_performance = 0 
                for pedido in pedidos_naquele_estado:
                    soma_das_performance += pedido.transportadora.performance
                if len(pedidos_naquele_estado)!=0:
                    media= soma_das_performance/ len(pedidos_naquele_estado)
                else: 
                    media=0
                context ['performance_media'].append({
                    'estado': estado,
                    'media': media,
                })
                    

            # context['estado_list'] = []
            # performance_estado = []
            # pedidos_por_estado = []

            # #algoritmo para calcular a media de performance por estado
            # for estado in estados:
            #     pedidos_por_estado.append(pedidos_filtrados.filter(UFDestino=estado))

            # for pedidos in pedidos_por_estado:
            #     performance_estado.append([pedido.transportadora.performance for pedido in pedidos])


            # for i in range(0, len(estados)):
            #     context['estado_list'].append({
            #         'estado': estados[i],
            #         'performance_media' : int(sum(performance_estado[i]) / len(performance_estado[i]))
            #         })
                    

            inicio_periodo = str(inicio.day) + '/' + str(inicio.month) + '/' + str(inicio.year) 
            context['inicio_periodo'] = inicio_periodo

            fim_periodo = str(fim.day) + '/' + str(fim.month) + '/' + str(fim.year) 
            context['fim_periodo'] = fim_periodo

            context['pedidos_list'] = pedidos_filtrados  
            context['transportadora_list'] = transportadoras


            path_template = 'graficos_performance.html'
            return render(request, path_template, context)

class GerarGraficoFinanceiro(View):
    def get(self, request):
        transportadoras = Transportadora.objects.all()
        context = {
                'transportadora_list' : transportadoras
                } 
        return render(request, 'criar_grafico_financeiro.html', context)

    
    def post(self, request):
        context = {}
        #pegando infos do post request
        inicio_periodo = request.POST.get('inicio-periodo')
        fim_periodo = request.POST.get('fim-periodo')
        estado = request.POST.getlist('estado')
        transportadora_pks = request.POST.getlist('transportadora')
        tipo_de_grafico = request.POST.get('tipo-de-grafico')

        #transformando string 'inicio-periodo' e 'fim-periodo' em datetime
        inicio = pandas.to_datetime(inicio_periodo).date()
        fim = pandas.to_datetime(fim_periodo).date()

        transportadoras = []
        estados = estado 
        #pegando objeto transportadora
        if 'ALL' in transportadora_pks:
            #filtrando pedidos 

            pedidos_filtrados = Pedido.objects.filter(
                    data_previsao__range=[inicio, fim],
                    UFDestino__in=estados,
                    )
            
            transportadoras = Transportadora.objects.all()

        else:
            for pk in transportadora_pks:
                transportadoras.append(Transportadora.objects.get(pk=int(pk)))

            pedidos_filtrados = Pedido.objects.filter(
                    data_previsao__range=[inicio, fim],
                    UFDestino__in=estados,
                    transportadora__in=transportadoras,
                    )
            context['transportadora_list'] = transportadoras


            context['estado_list'] = []
            for estado in estados:
                total_valor = 0
                pedidos_com_estado_em_questao = pedidos_filtrados.filter(UFDestino=estado)
                for pedido in pedidos_com_estado_em_questao:
                    total_valor += pedido.valor
                print(total_valor)
                context['estado_list'].append({
                    'total_valor' : total_valor,
                    'estado' : estado,
                    }) 


            datas_array = []
            data1 = inicio
            data2 = fim

            delta = data2 - data1


            for i in range(delta.days + 1):
                dia = data1 + datetime.timedelta(i)
                print(dia)
                datas_array.append(dia)

            valores_totais_dia=[]
            datas_padrao=[]
            for data in datas_array:
                pedidos_do_dia = Pedido.objects.filter(data_previsao=data)
                valor_total=0
                for pedido in pedidos_do_dia:
                    valor_total+= pedido.valor
                data_em_questao = str(data.day) + '/' + str(data.month) + '/' + str(data.year)
                datas_padrao.append({
                    'data': data_em_questao,
                    'valor': valor_total,
                    })
            context['datas_e_valores'] = datas_padrao


            context['transportadora_list2'] = []
            
            for transportadora in transportadoras:
                total_valor = 0
                pedidos_com_transportadora_em_questao = pedidos_filtrados.filter(transportadora=transportadora)
                for pedido in pedidos_com_transportadora_em_questao:
                    total_valor += pedido.valor
                context['transportadora_list2'].append({
                    'total' : total_valor,
                    'transportadora' : transportadora,
                    })

        

        inicio_periodo = str(inicio.day) + '/' + str(inicio.month) + '/' + str(inicio.year) 
        context['inicio_periodo'] = inicio_periodo

        fim_periodo = str(fim.day) + '/' + str(fim.month) + '/' + str(fim.year) 
        context['fim_periodo'] = fim_periodo

        path_template = 'graficos_financeiro.html'
        return render(request, path_template, context)

class GerarGraficoPendencia(View):
    def get(self, request):
        transportadoras = Transportadora.objects.all()
        context = {
                'transportadora_list' : transportadoras
                } 
        return render(request, 'criar_grafico_pendencia.html', context)

    def post(self, request):
        context = {}
        #pegando infos do post request
        inicio_periodo = request.POST.get('inicio-periodo')
        fim_periodo = request.POST.get('fim-periodo')
        estado = request.POST.getlist('estado')
        transportadora_pks = request.POST.getlist('transportadora')
        tipo_de_grafico = request.POST.get('tipo-de-grafico')

         #transformando string 'inicio-periodo' e 'fim-periodo' em datetime
        inicio = pandas.to_datetime(inicio_periodo).date()
        fim = pandas.to_datetime(fim_periodo).date()

        transportadoras = []
        estados = estado 
        #pegando objeto transportadora
        if 'ALL' in transportadora_pks:
            #filtrando pedidos 

            pedidos_filtrados = Pedido.objects.filter(
                    data_previsao__range=[inicio, fim],
                    UFDestino__in=estados,
                    )

            transportadoras = Transportadora.objects.all()

        else:
            for pk in transportadora_pks:
                transportadoras.append(Transportadora.objects.get(pk=int(pk)))

            pedidos_filtrados = Pedido.objects.filter(
                    data_previsao__range=[inicio, fim],
                    UFDestino__in=estados,
                    transportadora__in=transportadoras,
                    )

            context['estado_list'] = []
            for estado in estados:
                pedidos_pendente_com_estado_em_questao = pedidos_filtrados.filter(status="Pendente").filter(UFDestino=estado).count()
                context['estado_list'].append({
                    'total' : pedidos_pendente_com_estado_em_questao,
                    'estado' : estado,
                    }) 


            context['transportadora_list2'] = []

            for transportadora in transportadoras:
                pedidos_pendentes_com_transportadora_em_questao = pedidos_filtrados.filter(transportadora=transportadora).filter(status="Pendente").count()
                context['transportadora_list2'].append({
                    'total' : pedidos_pendentes_com_transportadora_em_questao,
                    'transportadora' : transportadora,
                    })


             # datas_array = []
            # data1 = inicio
            # data2 = fim

             # delta = data2 - data1


             # for i in range(delta.days + 1):
            #     dia = data1 + datetime.timedelta(i)
            #     print(dia)
            #     datas_array.append(dia)

             # datas_padrao=[]
            # for data in datas_array:
            #     pedidos_do_dia = Pedido.objects.filter(data_previsao=data).count()
            #     data_em_questao = str(data.day) + '/' + str(data.month) + '/' + str(data.year)
            #     datas_padrao.append({
            #         'data': data_em_questao,
            #         'total': pedidos_do_dia,
            #         })
            # context['datas_e_valores'] = datas_padrao





        inicio_periodo = str(inicio.day) + '/' + str(inicio.month) + '/' + str(inicio.year) 
        context['inicio_periodo'] = inicio_periodo

        fim_periodo = str(fim.day) + '/' + str(fim.month) + '/' + str(fim.year) 
        context['fim_periodo'] = fim_periodo

        path_template = 'grafico_pendencia.html'
        return render(request, path_template, context)



class CadastrarFuncionario(CreateView):
    form_class = FuncionarioForm
    template_name = "cadastrar_funcionario.html"
    #success_url = "/dash_consultor"
    def post(self, request):
        nome=request.POST.get('nome')
        senha=request.POST.get('senha')
        confirmar_senha=request.POST.get('confirmar_senha')
        email=request.POST.get('email')
        telefone=request.POST.get('telefone')
        print(nome, senha, confirmar_senha, email, telefone)


        if Funcionario.objects.filter(email=email).exists():
            context['erro'] = "Email já cadastrado no sistema"
            return render(request, "cadastrar_funcionario.html", context, locals())
        else:
            if senha == confirmar_senha:
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password='raw'
                )
                user.set_password(senha)
                user.save()

                funcionario = Funcionario.objects.create(
                    user=user,
                    nome=nome,
                    senha=senha,
                    email=email,
                    telefone=telefone
                )
                funcionario.save()
                send_mail(
                    'Login criado com sucesso!',
                    'Login:email',
                    'barbara.beltrami@hotmail.com',
                    [email],
                    fail_silently=False,
                    )


        return redirect('/')



class CadastrarAdministrador(CreateView):
    form_class = AdministradorForm
    template_name = "cadastrar_administrador.html"
    #success_url = "/dash_consultor"
    def post(self, request):
        nome=request.POST.get('nome')
        senha=request.POST.get('senha')
        confirmar_senha=request.POST.get('confirmar_senha')
        email=request.POST.get('email')
        telefone=request.POST.get('telefone')
        print(nome, senha, confirmar_senha, email, telefone)


        if Administrador.objects.filter(email=email).exists():
            context['erro'] = "Email já cadastrado no sistema"
            return render(request, "cadastrar_administrador.html", context, locals())
        else:
            if senha == confirmar_senha:
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password='raw'
                )
                user.set_password(senha)
                user.save()

                administrador = Administrador.objects.create(
                    user=user,
                    nome=nome,
                    senha=senha,
                    email=email,
                    telefone=telefone
                )
                administrador.save()


        return redirect('/')


class CadastrarProprietario(CreateView):
    #form_class = 
    template_name = "cadastrar_#.html"
    #success_url = "/dash_consultor"
    def post(self, request):
        nome=request.POST.get('nome')
        senha=request.POST.get('senha')
        confirmar_senha=request.POST.get('confirmar_senha')
        email=request.POST.get('email')
        telefone=request.POST.get('telefone')
        print(nome, senha, confirmar_senha, email, telefone)


        if Proprietario.objects.filter(email=email).exists():
            context['erro'] = "Email já cadastrado no sistema"
            return render(request, "cadastrar_#.html", context, locals())
        else:
            if senha == confirmar_senha:
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password='raw'
                )
                user.set_password(senha)
                user.save()

                proprietario = Proprietario.objects.create(
                    user=user,
                    nome=nome,
                    senha=senha,
                    email=email,
                    telefone=telefone
                )
                proprietario.save()




        return redirect('/')

class ListarFuncionarios(View):
    template_name = "listar_funcionarios.html"
    def get(self, request):
        context = {}
        context['lista_funcionarios'] = Funcionario.objects.all()
        return render(request, self.template_name, context)

    def post(self, request):
        return render(request, self.template_name, context)

class VerFuncionario(View):
    template_name = "ver_funcionario.html"
    def get(self, request, funcionario_id):
        context = {}
        funcionario = Funcionario.objects.get(id=funcionario_id)
        context['funcionario'] = Funcionario.objects.get(id=funcionario_id)
        return render(request, self.template_name, context)

    def post(self, request, funcionario_id):
        return render(request, self.template_name, context)

class EditarFuncionario(View):
    template_name = "alterar_funcionario.html"
    def get(self, request, pk):
        context = {}
        context['funcionario'] = Funcionario.objects.get(pk=pk)
        return render(request, self.template_name, context)

    def post(self, request, pk):
        context = {}
        context['funcionario'] = Funcionario.objects.get(pk=pk)
        context['erro'] = "Senha e Confirmação de Senha diferentes!"
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        print(nome, senha, confirmar_senha, email, telefone)

        if senha == confirmar_senha:
            funcionario = Funcionario.objects.get(pk=pk)
            
            funcionario.nome = nome
            funcionario.senha = senha
            funcionario.confirmar_senha = confirmar_senha
            funcionario.email = email
            funcionario.telefone = telefone
            funcionario.save()

            funcionario.user.username = email
            funcionario.user.email = email
            funcionario.user.password = 'raw'
            funcionario.user.set_password(senha)
            funcionario.user.save()
        
        else:
            return render(request, self.template_name, context)
        funcionario_pk = funcionario.pk


            #send_mail(
            #    'Usuario alterado com sucesso!',
            #    'Login:email',
            #    'barbara.beltrami@hotmail.com',
            #    [email],
            #    fail_silently=False,
            #    )


        return redirect('/funcionario/ver/'+  str(funcionario_pk))


class ListarAdministradores(View):
    template_name = "listar_administradores.html"
    def get(self, request):
        context = {}
        context['lista_administradores'] = Administrador.objects.all()
        return render(request, self.template_name, context)

    def post(self, request):
        return render(request, self.template_name, context)

class VerAdministrador(View):
    template_name = "ver_administrador.html"
    def get(self, request, administrador_id):
        context = {}
        administrador = Administrador.objects.get(id=administrador_id)
        context['administrador'] = Administrador.objects.get(id=administrador_id)
        return render(request, self.template_name, context)

    def post(self, request, funcionario_id):
        return render(request, self.template_name, context)

class EditarAdministrador(View):
    template_name = "alterar_administrador.html"
    def get(self, request, pk):
        context = {}
        context['administrador'] = Administrador.objects.get(pk=pk)
        return render(request, self.template_name, context)

    def post(self, request, pk):
        context = {}
        context['administrador'] = Administrador.objects.get(pk=pk)
        context['erro'] = "Senha e Confirmação de Senha diferentes!"
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        print(nome, senha, confirmar_senha, email, telefone)

        if senha == confirmar_senha:
            administrador = Administrador.objects.get(pk=pk)
            administrador.nome = nome
            administrador.senha = senha
            administrador.confirmar_senha = confirmar_senha
            administrador.email = email
            administrador.telefone = telefone
            
            administrador.save()

            administrador.user.username = email
            administrador.user.email = email
            administrador.user.password = 'raw'
            administrador.user.set_password(senha)
            
            administrador.user.save()
        
        else:
            return render(request, self.template_name, context)
        administrador_pk = administrador.pk


            #send_mail(
            #    'Usuario alterado com sucesso!',
            #    'Login:email',
            #    'barbara.beltrami@hotmail.com',
            #    [email],
            #    fail_silently=False,
            #    )


        return redirect('/administrador/ver/'+  str(administrador_pk))