# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.views.generic import View, TemplateView
from django.http import HttpResponse
# Create your views here.


class Login(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            print(request.user.__class__.__name__)
            return redirect('/usuarios/empresa')
        return render(request, 'login.html')

class EsqueciMinhaSenha(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'esqueci_minha_senha.html')


class DashboardEmpresa(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard_empresa.html')

class DashboardAdmin(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard_admin.html')

class DashboardOrganizador(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard_organizador.html')