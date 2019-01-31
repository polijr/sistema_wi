from django.db import models
from usuarios.models import Empresa

class Documento(models.Model):
	nome = models.CharField('Nome', max_length=100)
	arquivo = models.FileField(upload_to='documentos/files')
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=False)
	observacao = models.TextField('Observação', max_length=200)

	def __str__(self):
		return self.empresa.usuario.user.username + ' - ' + self.nome