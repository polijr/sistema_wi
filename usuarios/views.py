# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.views.generic import View, TemplateView
from django.http import HttpResponse
# Create your views here.
def login(request):
    return render(request, 'erro_500.html')

def esqueci_minha_senha(request):
    return render(request, 'esqueci_minha_senha.html')


def dashboard_empresa(request):
    return render(request, 'dashboard_empresa.html')

def dashboard_admin(request):
    return render(request, 'dashboard_admin.html')

def dashboard_organizador(request):
    return render(request, 'dashboard_organizador.html')