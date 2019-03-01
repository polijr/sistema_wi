from django.db import models
from usuarios.models import Empresa
import os


class Documento(models.Model):
	nome = models.CharField('Nome', max_length=100)
	arquivo = models.FileField(upload_to='documentos/files')
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=False, related_name='arquivo_empresa')
	observacao = models.TextField('observacao', max_length=200, blank = True)
	data = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.empresa.usuario.user.username + ' - ' + self.nome

	def filename(self):
		return os.path.basename(self.arquivo.name)



class NotaFiscal(models.Model):
	nome = models.CharField('Nome', max_length=100)
	arquivo = models.FileField(upload_to='documentos/files')
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=False, related_name='nota_empresa')
	observacao = models.TextField('observacao', max_length=200, blank = True)
	data = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.empresa.usuario.user.username + ' - ' + self.nome

