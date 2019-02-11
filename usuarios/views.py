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
from .forms import *
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
        if  request.user.usuario.cargo != 0:
            return render(request, 'erro_403.html')
        informes_list = Informe.objects.all().order_by("-data")

        paginator = Paginator(informes_list, 3) # Show 25 contacts per page

        page = request.GET.get('page')
        informes = paginator.get_page(page)
        return render(request, 'dashboard_empresa.html', {'informes' : informes})

class DashboardAdmin(View):
    def get(self, request, *args, **kwargs):
        if  request.user.usuario.cargo != 2:
            return render(request, 'erro_403.html')
        return render(request, 'dashboard_admin.html')

class DashboardOrganizador(View):
    def get(self, request, *args, **kwargs):
        if  request.user.usuario.cargo != 1:
            return render(request, 'erro_403.html')
        pedidos = Pedido.objects.all().order_by("data")
        return render(request, 'dashboard_organizador.html', {"pedidos":pedidos})

class DashboardCaravaneiro(View):
    def get(self, request, *args, **kwargs):
        if  request.user.usuario.cargo != 3:
            return render(request, 'erro_403.html')
        pedidos = Pedido.objects.all().order_by("data")
        return render(request, 'dashboard_caravaneiro.html', {"pedidos":pedidos})

class Redirecionar(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.usuario.cargo == 0:
                return redirect('/usuarios/empresa')
            if request.user.usuario.cargo == 1:
                return redirect('/usuarios/organizador')
            if request.user.usuario.cargo == 2:
                return redirect('/usuarios/admin')
            if request.user.usuario.cargo == 3:
                return redirect('/usuarios/caravaneiro')
            else:
               return redirect('/admin') 

class CadastroEmpresa(View):
    def get(self, request, *args, **kwargs):
        if  request.user.usuario.cargo != 1 and request.user.usuario.cargo != 2:
            return render(request, 'erro_403.html')
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
        if  request.user.usuario.cargo != 2:
            return render(request, 'erro_403.html')
        return render(request, 'cadastro_organizador.html')

    def post(self, request, *args, **kwargs):
        form = CadastroOrganizadorForm(request.POST)
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
    def get(self, request, pk, *args, **kwargs):
        empresa = Empresa.objects.get(pk=pk)
        organizadores = Organizador.objects.all()
        if request.user.usuario.cargo == 1:
            template_base = 'base_menus_organizador.html'
        elif request.user.usuario.cargo == 2:
            template_base = 'base_menus_admin.html'
        else:
            return render(request, 'erro_403.html')
        return render(request, 'editar_empresa.html', {'empresa': empresa, 'organizadores': organizadores, 'template_base': template_base})

    def post(self, request, pk, *args, **kwargs):
        
        empresa = Empresa.objects.get(pk=pk)
        empresa.nome = request.POST["nome"]
        empresa.stand = int(request.POST["stand"])
        empresa.cnpj = request.POST["cnpj"]
        empresa.usuario.user.username = request.POST["username"]
        empresa.tamanho = request.POST["tamanho"]
        empresa.palestra = request.POST["palestra"]
        empresa.organizador_resp = Organizador.objects.get(pk=request.POST["organizador_resp"])
        empresa.save()
        empresa.usuario.user.save()
        if request.user.usuario.cargo == 1:
            return HttpResponseRedirect('/usuarios/minhas-empresas')
        if request.user.usuario.cargo == 2:
            return HttpResponseRedirect('/usuarios/todas-empresas')

class EditarOrganizador(View):
    def get(self, request, pk, *args, **kwargs):
        if request.user.usuario.cargo == 2:
            organizador = Organizador.objects.get(pk=pk)
            return render(request, 'editar_organizador.html', {'organizador': organizador})
        else:
            return render(request, 'erro_403.html')

    def post(self, request, pk, *args, **kwargs):
        request.POST._mutable = True
        request.POST['pk']=pk
        form = EditarOrganizadorForm(request.POST)
        print(form)
        if form.is_valid():
            organizador = Organizador.objects.get(pk=pk)
            organizador.nome = request.POST["nome"]
            organizador.sobrenome = request.POST["sobrenome"]
            organizador.usuario.user.username = request.POST["username"]
            organizador.email = request.POST["email"]
            organizador.telefone = request.POST["telefone"]
            organizador.save()
            organizador.usuario.user.save()
            return HttpResponseRedirect('/usuarios/todos-organizadores')
        organizador = Organizador.objects.get(pk=pk)
        return render(request, 'editar_organizador.html', {'organizador': organizador, 'form': form})

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
        if request.user.usuario.cargo == 1:
            user_organizador = request.user.usuario.usuario_organizador
            empresa = Empresa.objects.filter(organizador_resp = user_organizador)
            template_base = 'base_menus_organizador.html'
        elif request.user.usuario.cargo == 2:
            empresa = Empresa.objects.all()
            template_base = 'base_menus_admin.html'
        else:
            return render(request, 'erro_403.html')
        return render(request, 'empresas_do_organizador.html', {'empresa': empresa, 'template_base': template_base})

class TodosOrganizadores(View):
    def get(self, request, *args, **kwargs):
        if request.user.usuario.cargo == 2:
            organizadores = Organizador.objects.all()
            return render(request, 'todos_organizadores.html', {'organizadores': organizadores})
        else:
            return render(request, 'erro_403.html')

class CadastroCaravaneiro(View):
    def get(self, request, *args, **kwargs):
        if request.user.usuario.cargo != 2:
            return render(request, 'erro_403.html')
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

class TodasEmpresas(View):
    def get(self, request, *args, **kwargs):
        empresa = Empresa.objects.all()
        return render(request, 'todas_empresas.html', {'empresa': empresa})

class TodosCaravaneiros(View):
    def get(self, request, *args, **kwargs):
        caravaneiro = Caravaneiro.objects.all()
        return render(request, 'todos_caravaneiros.html', {'caravaneiro': caravaneiro}) 

class PerfilGerente(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        user_gerente = user.usuario
        gerente = Gerente.objects.get(usuario = user_gerente)
        return render(request, 'perfil_gerente.html', {'gerente': gerente, 'user': user})

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['pk']=int(request.user.usuario.usuario_gerente.pk)
        print(request.POST)
        form = EditarGerenteForm(request.POST)
        if form.is_valid():
            gerente = Gerente.objects.filter()[0]
            gerente.usuario.user.first_name = request.POST["nome"]
            gerente.usuario.user.last_name = request.POST["sobrenome"]
            gerente.usuario.user.username = request.POST["username"]
            gerente.usuario.user.email = request.POST["email"]
            if request.POST["password"]!='':
                if request.POST["password"]==request.POST["password2"]:
                    gerente.usuario.user.set_password(request.POST["password"])
                    gerente.save()
                    gerente.usuario.user.save()
            else:
                gerente.save()
                gerente.usuario.user.save()
            return HttpResponseRedirect('/usuarios/admin')
        else:
            user = request.user
            user_gerente = user.usuario
            gerente = Gerente.objects.get(usuario = user_gerente)
            return render(request, 'perfil_gerente.html', {'form': form, 'gerente': gerente, 'user': user})

class EditarCaravaneiro(View):
    def get(self, request, pk, *args, **kwargs):
        if request.user.usuario.cargo == 2:
            caravaneiro = Caravaneiro.objects.get(pk=pk)
            return render(request, 'editar_caravaneiro.html', {'caravaneiro': caravaneiro})
        else:
            return render(request, 'erro_403.html')
    
    def post(self, request, pk, *args, **kwargs):
        request.POST._mutable = True
        request.POST['pk']=pk
        form = EditarCaravaneiroForm(request.POST)
        if form.is_valid():
            caravaneiro = Caravaneiro.objects.get(pk=pk)
            caravaneiro.nome = request.POST["nome"]
            caravaneiro.sobrenome = request.POST["sobrenome"]
            caravaneiro.usuario.user.username = request.POST["username"]
            caravaneiro.email = request.POST["email"]
            caravaneiro.telefone = request.POST["telefone"]
            caravaneiro.save()
            caravaneiro.usuario.user.save()
            return HttpResponseRedirect('/usuarios/todos-caravaneiros')
        caravaneiro = Caravaneiro.objects.get(pk=pk)
        return render(request, 'editar_caravaneiro.html', {'form' : form, 'caravaneiro': caravaneiro})

class PerfilCaravaneiro(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        user_caravaneiro = user.usuario
        caravaneiro = Caravaneiro.objects.get(usuario = user_caravaneiro)
        return render(request, 'perfil_caravaneiro.html', {'caravaneiro': caravaneiro})