from django.db import models

class Type(models.Model):
	name = models.CharField('Nome', unique=True, max_length=100)
	image = models.ImageField(upload_to='pedidos/images', verbose_name='Imagem', blank=True, null=True)

	def __str__(self):
		return self.name 

	class Meta:
		verbose_name = 'Tipo de Pedido'
		verbose_name_plural = 'Tipos de Pedido'
