from django.db import models
from datetime import datetime 

import datetime
from datetime import date

class Type(models.Model):
	name = models.CharField('Nome', unique=True)
	image = models.ImageField(upload_to='pedidos/images', verbose_name='Imagem', blank=True, null=True)

	def __str__(self):
		return self.name 

	class Meta:
		verbose_name = 'Tipo de Pedido'
		verbose_name_plural = 'Tipos de Pedido'


class Pedidos(models.Model):
	data = models.DateField(auto_now_add=True, blank=True, null=True)
	tipo = models.ForeignKey(Type, on_delete=models.CASCADE, null=False)
	caravaneiro = models.BooleanField(default=False)
	organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE, null=False)


