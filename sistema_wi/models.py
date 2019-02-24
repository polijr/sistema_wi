# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db import models
from datetime import date

class dataFeed(models.Model):
    link = models.CharField('link' , null = True, blank = True, max_length = 1000)
    data = models.DateField('data', null =  True, blank = True)
    dataCriado = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'dataFeed'
        verbose_name_plural = 'dataFeeds'


class ValoresEstaticos(models.Model):
    ano_wi = models.CharField(null = False, default="29", blank = False, max_length=5)
    nome_wifi = models.CharField(null = False, default="polijunior", blank = False, max_length=100)
    senha_wifi = models.CharField(null = False, default="polijunior", blank = False, max_length=100)
    data_de_inicio = models.DateField(null=False, blank=False, default=None)
    mapa_wi = models.ImageField(null = True, blank = True, upload_to = 'sistema_wi/fotos')
    calendario_wi = models.ImageField(null=True, blank=True, upload_to='sistema_wi/fotos')

    def __str__(self):
        return "APENAS ALTERAR, NÃO CRIAR!"

    class Meta:
    	verbose_name = 'Valores Estaticos'
    	verbose_name_plural = 'Valores Estaticos'    