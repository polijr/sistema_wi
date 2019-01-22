from django.contrib import admin
from core.models import *
from .views import *
# Register your models here.
admin.site.register(Transportadora)
admin.site.register(Registro)
admin.site.register(ProgramacaoTransporte)
admin.site.register(Pedido)
admin.site.register(Prazo)
admin.site.register(Valor)
admin.site.register(RegraDeNegocio)
admin.site.register(Tabela_Precos)
admin.site.register(Tabela_Prazos)
admin.site.register(RastreamentoArquivo)
admin.site.register(Funcionario)
admin.site.register(Administrador)







