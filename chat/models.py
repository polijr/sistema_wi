from django.db import models
from usuarios.models import Usuario

class Mensagem(models.Model):
	texto = models.TextField("Mensagem", max_length=200, blank=False)
	data = models.DateTimeField(auto_now_add=True, null=False)
	emissor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, related_name='mensagens_emitidas')
	receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, related_name='mensagens_recebidas')

	def __str__(self):
		return self.emissor.user.username + ' - ' + self.data.strftime('%d/%m/%Y às %Hh%Mmin')

	class Meta:
		verbose_name = 'Mensagem'
		verbose_name_plural = 'Mensagens'