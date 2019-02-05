# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



class ValoresEstaticos(models.Model):
    ano_wi = models.CharField(null = False, default="29", blank = False, max_length=5)
    nome_wifi = models.CharField(null = False, default="polijunior", blank = False, max_length=100)
    senha_wifi = models.CharField(null = False, default="polijunior", blank = False, max_length=100)
    data_de_inicio = models.DateField(null=False, blank=False, default=None)

    def __str__(self):
        return "APENAS ALTERAR, NÃO CRIAR!"

    class Meta:
    	verbose_name = 'Valores Estaticos'
    	verbose_name_plural = 'Valores Estaticos'