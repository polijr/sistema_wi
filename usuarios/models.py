# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Usuario(models.Model):
    CARGO_CHOICES = (
        (0, "Empresa"),
        (1, "Organizador"),
        (2, "Gerente"),
    )
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=False, related_name = 'usuario')
    cargo = models.IntegerField(choices=CARGO_CHOICES, null=False, blank=False)