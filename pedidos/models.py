from django.db import models
from datetime import datetime

import datetime
from datetime import date
from usuarios.models import Usuario, Organizador

class Type(models.Model):
	name = models.CharField('Nome', unique=True, max_length=100)
	image = models.ImageField(upload_to='pedidos/images', verbose_name='Imagem', blank=True, null=True)

	def __str__(self):
		return self.name 

	class Meta:
		verbose_name = 'Tipo de Pedido'
		verbose_name_plural = 'Tipos de Pedido'


class Pedido(models.Model):
	data = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	tipo = models.ForeignKey(Type, on_delete=models.CASCADE, null=False)
	organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE, null=True)
	pedinte = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
	observacao = models.TextField("Observação", max_length=200, blank=True)
	def __str__(self):
		return self.tipo.name

	class Meta:
		verbose_name = "Pedido"
		verbose_name_plural = "Pedidos"
