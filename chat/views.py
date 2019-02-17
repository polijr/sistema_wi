from django.shortcuts import render
from django.views.generic import View
from usuarios.models import Usuario
from .models import Mensagem
from usuarios.models import *
from django.http import JsonResponse
from itertools import zip_longest
from itertools import chain
from django.db.models import Q




class CriarMensagem(View):
	def post(self, request, *args, **kwargs):
		mensagem = Mensagem(texto=request.POST["texto"], emissor=request.user.usuario, receptor=Usuario.objects.get(pk=request.POST["pk"]))
		mensagem.save()
		return JsonResponse({'criou': True})

class CarregarMensagens(View):
	def get(self, request, pk, *args, **kwargs):
		usuario = request.user.usuario
		intelocutor = Usuario.objects.get(pk=pk)
		mensagens = Mensagem.objects.filter(Q(emissor=usuario, receptor=intelocutor) | Q(emissor=intelocutor, receptor=usuario)).order_by("data").values()
		mensagens_json = list(mensagens)
		return JsonResponse(mensagens_json, safe=False)

		
class MensagensNaoVisualizadas(View):
	def get(self, request, pk, *args, **kwargs):
		usuario = request.user.usuario
		intelocutor = Usuario.objects.get(pk=pk)
		mensagens = Mensagem.objects.filter(Q(emissor=usuario, receptor=intelocutor, recebeu=False) | Q(emissor=intelocutor, receptor=usuario, recebeu = False)).order_by("data").values()
		mensagens_json = list(mensagens)
		for mensagem in mensagens_json:
			m = Mensagem.objects.get(pk=mensagem['id'])
			m.recebeu = True
			m.save()
		return JsonResponse(mensagens_json, safe=False)



class RecebeuMensagem(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo != 0 and request.user.usuario.cargo != 1:
			return render(request, 'erro_403.html')
		if request.user.usuario.cargo == 0:
			interlocutores = [request.user.usuario.usuario_empresa.organizador_resp]
		else:
			interlocutores = Empresa.objects.filter(organizador_resp=request.user.usuario.usuario_organizador)
		recebeu = []
		if Mensagem.objects.filter(receptor=request.user.usuario, recebeu=False).exists():
			recebeu.append(True)
		else: recebeu.append(False)
		for interlocutor in interlocutores:
			if Mensagem.objects.filter(emissor=interlocutor.usuario, receptor=request.user.usuario, recebeu=False).exists():
				recebeu.append(True)
			else: recebeu.append(False)
		return JsonResponse(recebeu, safe=False)



class Chat(View):
	def get(self, request, pk,*args, **kwargs):
		receptor = Usuario.objects.get(pk=pk)
		if request.user.usuario.cargo == 1:
			template_base = 'base_menus_organizador.html'
		elif request.user.usuario.cargo == 0:
			template_base = 'base_menus_empresa.html'
		else:
			return render(request, 'erro_403.html')
		return render(request, 'chat.html', {'template_base': template_base, 'receptor':receptor})













# class CarregarMensagens(View):
# 	def get(self, request, pk, *args, **kwargs):
# 		usuario = request.user.usuario
# 		intelocutor = Usuario.objects.get(pk=pk)
# 		mensagens_recebidas = Mensagem.objects.filter(emissor=intelocutor, receptor=usuario).order_by("data")
# 		mensagens_enviadas = Mensagem.objects.filter(emissor=usuario, receptor=intelocutor).order_by("data")
# 		dados_recebidas = []
# 		dados_enviadas = []
# 		for mensagem_recebida, mensagem_enviada in zip_longest(mensagens_recebidas, mensagens_enviadas):
# 			if mensagem_recebida != None and ((not mensagem_recebida.recebeu) or request.GET["primeira_vez"] == 'Sim'):
# 				mensagem_recebida.recebeu = True
# 				mensagem_recebida.save()
# 				dados_recebidas.append({
# 					'texto': mensagem_recebida.texto,
# 					'data': mensagem_recebida.data
# 				})
# 			if mensagem_enviada != None and (not mensagem_enviada.recebeu or request.GET["primeira_vez"] == 'Sim'):
# 				mensagem_enviada.recebeu = True
# 				mensagem_enviada.save()
# 				dados_enviadas.append({
# 					'texto': mensagem_enviada.texto,
# 					'data': mensagem_enviada.data
# 				})
# 		dados = {
# 			'dados_recebidas': dados_recebidas,
# 			'dados_enviadas': dados_enviadas
# 		}
# 		return JsonResponse(dados)

