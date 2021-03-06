# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



class Usuario(models.Model):
    CARGO_CHOICES = (
        (0, "Empresa"),
        (1, "Organizador"),
        (2, "Gerente"),
        (3, "Caravaneiro")
    )
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = False, related_name = 'usuario')
    cargo = models.IntegerField(choices = CARGO_CHOICES, null = False, blank = False)
    enviou_mensagem = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

class Gerente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, related_name = 'usuario_gerente', null = False, blank = False)
    def __str__(self):
        return self.usuario.user.username

class Organizador(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, related_name = 'usuario_organizador', null = False, blank = False)
    nome = models.CharField(null = False, blank = False, max_length=100)
    sobrenome = models.CharField(null = False, blank = False, max_length=100)
    telefone = models.CharField(null = False, blank = False, max_length=100)
    email = models.EmailField(null = False, blank = False, max_length=100)
    def __str__(self):
        return self.usuario.user.username
    class Meta:
        verbose_name = 'Organizador'
        verbose_name_plural = 'Organizadores'

class Empresa(models.Model):    
    TAMANHO_CHOICES = (
        (0, "9 m2"),
        (1, "10 m2"),
        (2, "10,5 m2"),
        (3, "12 m2"),
        (4, "14 m2"),
        (5, "20 m2"),
        (6, "25,5 m2"),
        (7, "30 m2"),
        (8, "40 m2"),
        (9, "51,5 m2")
    )
    usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, related_name = 'usuario_empresa', null = False, blank = False)
    nome = models.CharField(null = False, blank = False, max_length=100)
    stand = models.IntegerField(null = False, blank = False)
    tamanho = models.IntegerField(choices = TAMANHO_CHOICES, null = False, blank = False)
    palestra = models.BooleanField(default = False, null = False, blank = False)
    organizador_resp = models.ForeignKey(Organizador,related_name="empresa_organizador", on_delete = models.CASCADE, null = False, blank = False)
    cnpj = models.CharField(max_length = 20, null = False, blank = False)
    def __str__(self):
        return self.usuario.user.username

class Caravaneiro(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE, related_name = 'usuario_caravaneiro', null = False, blank = False)
    nome = models.CharField(null = False, blank = False, max_length=100)
    sobrenome = models.CharField(null = False, blank = False, max_length=100)
    telefone = models.CharField(null = False, blank = False, max_length=100)
    email = models.EmailField(null = False, blank = False, max_length=100)
    def __str__(self):
        return self.usuario.user.username

class ResetSenha(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    chave = models.CharField(max_length=12, blank=False, null=False, unique=True)
    data = models.DateTimeField(auto_now_add=True)
