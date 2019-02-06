from django.db import models
from datetime import datetime

import datetime
from datetime import date
from usuarios.models import Usuario, Organizador

class Informe(models.Model):
	titulo = models.CharField('Titulo', max_length=100)
    texto = models.CharField('Texto')
    data = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name 

	class Meta:
		verbose_name = 'Informe'
		verbose_name_plural = 'Informes'

