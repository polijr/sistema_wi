# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Usuario, Organizador, Empresa, Gerente, Caravaneiro
from sistema_wi.models import ValoresEstaticos, dataFeed
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Organizador)
admin.site.register(Gerente)
admin.site.register(Empresa)
admin.site.register(ValoresEstaticos)
admin.site.register(Caravaneiro)
admin.site.register(dataFeed)