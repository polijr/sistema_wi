# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Usuario, Organizador, Empresa, Gerente
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Organizador)
admin.site.register(Gerente)
admin.site.register(Empresa)