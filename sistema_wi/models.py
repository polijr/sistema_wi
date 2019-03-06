# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db import models
from datetime import date
from usuarios.models import *

class dataFeed(models.Model):
    data = models.DateField('data', null =  True, blank = True)
    dataCriado = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return "DATA DE FEEDBACK"

    class Meta:
        verbose_name = 'dataFeed'
        verbose_name_plural = 'dataFeeds'


class LinkFeed(models.Model):
    nome = models.CharField('nome' , null = True, blank = True, max_length = 1000)
    link = models.CharField('link' , null = True, blank = True, max_length = 1000)


        
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Link de Feedback'
        verbose_name_plural = 'Links de Feedback'

class CheckFeed (models.Model): 
    empresa= models.ForeignKey(Empresa,related_name="feedback_empresa", on_delete = models.CASCADE, null = False, blank = False)
    feedback= models.ForeignKey(LinkFeed,related_name="feedback", on_delete = models.CASCADE, null = False, blank = False)
    status = models.BooleanField(default=False)

class ValoresEstaticos(models.Model):
    ano_wi = models.CharField(null = False, default="29", blank = False, max_length=5)
    nome_wifi = models.CharField(null = False, default="polijunior", blank = False, max_length=100)
    senha_wifi = models.CharField(null = False, default="polijunior", blank = False, max_length=100)
    data_de_inicio = models.DateField(null=False, blank=False, default=None)
    mapa_wi = models.FileField(null = True, blank = True, upload_to = 'sistema_wi/fotos')
    calendario_wi = models.FileField(null=True, blank=True, upload_to='sistema_wi/fotos')
    horario_massagem_inicio = models.TimeField(null=False)
    horario_massagem_fim = models.TimeField(null=False)
    intervalo_massagem = models.IntegerField()
    n_salas = models.IntegerField()

    def __str__(self):
        return "APENAS ALTERAR, NÃO CRIAR!"

    class Meta:
    	verbose_name = 'Valores Estaticos'
    	verbose_name_plural = 'Valores Estaticos'    
