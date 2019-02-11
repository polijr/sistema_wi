from django.shortcuts import render
from django.views.generic import View
from usuarios.models import Usuario
from .models import Mensagem
from django.http import JsonResponse
from itertools import zip_longest

class CarregarMensagens(View):
	def get(self, request, *args, **kwargs):
		usuario = request.user.usuario
		intelocutor = Usuario.objects.get(pk=request.GET['pk'])
		mensagens_recebidas = Mensagem.objects.filter(emissor=intelocutor, receptor=usuario).order_by("data")
		mensagens_enviadas = Mensagem.objects.filter(emissor=usuario, receptor=intelocutor).order_by("data")
		dados_recebidas = []
		dados_enviadas = []
		for mensagem_recebida, mensagem_enviada in zip_longest(mensagens_recebidas, mensagens_enviadas):
			if mensagem_recebida != None:
				dados_recebidas.append({
					'texto': mensagem_recebida.texto,
					'data': mensagem_recebida.data
				})
			if mensagem_enviada != None:
				dados_enviadas.append({
					'texto': mensagem_enviada.texto,
					'data': mensagem_enviada.data
				})
		dados = {
			'dados_recebidas': dados_recebidas,
			'dados_enviadas': dados_enviadas
		}
		return JsonResponse(dados)


