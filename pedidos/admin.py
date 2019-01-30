from django.contrib import admin
from .models import *


class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('data',)

admin.site.register(Type)
admin.site.register(Pedido, PedidoAdmin)

