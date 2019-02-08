# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .forms import CadastroEmpresaForm
from .forms import CadastroOrganizadorForm
from .forms import CadastroCaravaneiroForm
from django.contrib.auth.models import User
from django.contrib.auth import (login as auth_login,
    logout as auth_logout,
)
from .models import *
from django.http import HttpResponseRedirect
from informes.models import Informe
from informes.forms import InformeForm
from django.core.paginator import Paginator

# Create your views here.
from pedidos.models import *



class EsqueciMinhaSenha(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'esqueci_minha_senha.html')


class DashboardEmpresa(View):
    def get(self, request, *args, **kwargs):
        informes_list = Informe.objects.all().order_by("-data")

        paginator = Paginator(informes_list, 3) # Show 25 contacts per page

        page = request.GET.get('page')
        informes = paginator.get_page(page)
        return render(request, 'dashboard_empresa.html', {'informes' : informes})

class DashboardAdmin(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard_admin.html')

class DashboardOrganizador(View):
    def get(self, request, *args, **kwargs):
        pedidos = Pedido.objects.all().order_by("data")
        return render(request, 'dashboard_organizador.html', {"pedidos":pedidos})

class Redirecionar(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.usuario.cargo == 0:
                return redirect('/usuarios/empresa')
            if request.user.usuario.cargo == 1:
                return redirect('/usuarios/organizador')
            if request.user.usuario.cargo == 2:
                return redirect('/usuarios/admin')  
            else:
               return redirect('/admin') 

class CadastroEmpresa(View):
    def get(self, request, *args, **kwargs):
        organizadores = Organizador.objects.all()
        return render(request, 'cadastro_empresa.html', {'organizadores': organizadores})

    def post(self, request, *args, **kwargs):
        form = CadastroEmpresaForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username= form.data['username'],
                                            email=form.data['email'],
                                            password=form.data['password'])
            user.save()
            usuario = Usuario.objects.create(
                user=user,
                cargo=0)
            usuario.save()
            organizador = Organizador.objects.get(pk=request.POST["organizador_resp"])
            empresa = Empresa.objects.create(
                usuario = usuario,
                nome = request.POST["nome"],
                stand = request.POST["stand"],
                tamanho = request.POST["tamanho"],
                palestra = request.POST["palestra"],
                organizador_resp = organizador,
                cnpj = request.POST["cnpj"],
            )
            empresa.save()
            return HttpResponseRedirect('/usuarios/admin')

        organizadores = Organizador.objects.all()
        return render(request, 'cadastro_empresa.html', {'form': form, 'organizadores': organizadores})



class CadastroOrganizador(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cadastro_organizador.html')

    def post(self, request, *args, **kwargs):
        form = CadastroOrganizadorForm(request.POST)
        print(form)
        if form.is_valid():
            user = User.objects.create_user(username= form.data['username'],
                                            email=form.data['email'],
                                            password=form.data['password'],
                                            first_name=form.data["nome"],
                                            last_name=form.data["sobrenome"])
            user.save()
            usuario = Usuario.objects.create(user=user, cargo=1)
            usuario.save()
            organizador = Organizador.objects.create(
                usuario = usuario,
                nome = request.POST["nome"],
                sobrenome = request.POST["sobrenome"],
                telefone = request.POST["telefone"],
                email = request.POST["email"],
            )
            return HttpResponseRedirect('/usuarios/admin')
        return render(request, 'cadastro_organizador.html', {'form': form})

class EditarEmpresa(View):
    def get(self, request, pk):
        empresa = Empresa.objects.get(pk=pk)
        organizadores = Organizador.objects.all()
        return render(request, 'editar_empresa.html', {'empresa': empresa, 'organizadores': organizadores})

    def post(self, request, pk, *args, **kwargs):
        empresa = Empresa.objects.filter(pk=pk)
        nome = request.POST["nome"]
        stand = int(request.POST["stand"])
        cnpj = request.POST["cnpj"]
        organizador_resp = Organizador.objects.get(pk=request.POST["organizador_resp"])
        tamanho = request.POST["tamanho"]
        palestra = request.POST["palestra"]
        empresa.update(
            nome = nome,
            stand = stand,
            cnpj = cnpj,
            organizador_resp = organizador_resp,
            tamanho = tamanho,
            palestra = palestra
        )
        return HttpResponseRedirect('/usuarios/minhas-empresas')

class PerfilEmpresa(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        user_empresa = user.usuario
        empresa = Empresa.objects.get(usuario = user_empresa)
        if  not empresa.palestra:
            tem_palestra = "Não"
        else:
            tem_palestra = "Sim"
        return render(request, 'perfil_empresa.html', {'empresa': empresa, 'user': user, 'tem_palestra': tem_palestra})

class PerfilOrganizador(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        user_organizador = user.usuario
        organizador = Organizador.objects.get(usuario = user_organizador)
        return render(request, 'perfil_organizador.html', {'organizador': organizador, 'user': user})

class MinhasEmpresas(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        user_organizador = user.usuario.usuario_organizador
        empresa = Empresa.objects.filter(organizador_resp = user_organizador)
        return render(request, 'empresas_do_organizador.html', {'empresa': empresa})

class CadastroCaravaneiro(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cadastro_caravaneiro.html')

    def post(self, request, *args, **kwargs):
        form = CadastroCaravaneiroForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username= form.data['username'],
                                            email=form.data['email'],
                                            password=form.data['password'],
                                            first_name=form.data["nome"],
                                            last_name=form.data["sobrenome"])
            user.save()
            usuario = Usuario.objects.create(user=user, cargo=3)
            usuario.save()
            caravaneiro = Caravaneiro.objects.create(
                usuario = usuario,
                nome = request.POST["nome"],
                sobrenome = request.POST["sobrenome"],
                telefone = request.POST["telefone"],
                email = request.POST["email"],
            )
            return HttpResponseRedirect('/usuarios/admin')
        return render(request, 'cadastro_caravaneiro.html', {'form': form})