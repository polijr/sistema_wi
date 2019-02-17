from django.shortcuts import render
from django.views.generic import View
from usuarios.models import Usuario
from .models import Mensagem
from django.http import JsonResponse
from itertools import zip_longest



class CriarMensagem(View):
	def post(self, request, *args, **kwargs):
		mensagem = Mensagem(texto=request.POST["texto"], emissor=request.user.usuario, receptor=Usuario.objects.get(pk=request.POST["pk"]))
		mensagem.save()
		return JsonResponse({'criou': True})

class CarregarMensagens(View):

	# recomendacao do gabs: 
	# Adicionar no model de msg um atributo bool 'visualizada'
	# Assim que abrir tela de chat, puxar todas as msgs
	# Quando ja estiver aberta, puxar apenas os com atributo visualizada = false,
	# e alterar pra true assim q for puxada (economiza dados e processamento)
	# NECESSARIO:
	# criar endpoint que recebe post e cria a msg no banco de dados, 
	# enquanto altera o atributo recebeu mensagem de usuario pra true. Assim q todas as msgs forem puxadas,
	# sempre lembrar de alterar atributo pra false (pode ser tbm quando acessar a pagina de msgs, melhor assim na vdd).
	# Não precisa se preocupar no caso do organizador, em que mesmo que ele leia apenas de uma conversa,
	# o atributo vai virar false. Já é suficiente

	def get(self, request, *args, **kwargs):
		usuario = request.user.usuario
		intelocutor = Usuario.objects.get(pk=request.GET['pk'])
		mensagens_recebidas = Mensagem.objects.filter(emissor=intelocutor, receptor=usuario).order_by("data")
		mensagens_enviadas = Mensagem.objects.filter(emissor=usuario, receptor=intelocutor).order_by("data")
		dados_recebidas = []
		dados_enviadas = []
		for mensagem_recebida, mensagem_enviada in zip_longest(mensagens_recebidas, mensagens_enviadas):
			if mensagem_recebida != None and ((not mensagem_recebida.recebeu) or request.GET["primeira_vez"] == 'Sim'):
				mensagem_recebida.recebeu = True
				mensagem_recebida.save()
				dados_recebidas.append({
					'texto': mensagem_recebida.texto,
					'data': mensagem_recebida.data
				})
			if mensagem_enviada != None and (not mensagem_enviada.recebeu or request.GET["primeira_vez"] == 'Sim'):
				mensagem_enviada.recebeu = True
				mensagem_enviada.save()
				dados_enviadas.append({
					'texto': mensagem_enviada.texto,
					'data': mensagem_enviada.data
				})
		dados = {
			'dados_recebidas': dados_recebidas,
			'dados_enviadas': dados_enviadas
		}
		return JsonResponse(dados)


class RecebeuMensagem(View):
	def get(self, request, *args, **kwargs):
		return JsonResponse({'recebeu': Mensagem.objects.filter(receptor=request.user.usuario, recebeu=False).exists()})



class Chat(View):
    def get(self, request, *args, **kwargs):
        if request.user.usuario.cargo == 1:
            template_base = 'base_menus_organizador.html'
        elif request.user.usuario.cargo == 0:
            template_base = 'base_menus_empresa.html'
        else:
            return render(request, 'erro_403.html')
        return render(request, 'chat.html', {'template_base': template_base})

