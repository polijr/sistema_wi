from django.shortcuts import render
from django.views.generic import View
from .models import Type, Pedido
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from django.contrib import messages
import json
import datetime

class CarregarPedidos(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo == 1:
			dados = []
			for pedido in Pedido.objects.all().order_by("data"):
				if(pedido.pedinte.cargo == 3):
					dados.append({
						"tipo_pedido": pedido.tipo.name,
						"nome": pedido.pedinte.user.username,
						"tipo_pedinte": 'Caravaneiro',
						"observacao": pedido.observacao,
						"pk": pedido.pk
					})
			for pedido in Pedido.objects.all().order_by("data"):
				if(pedido.pedinte.cargo == 0):
					dados.append({
						"tipo_pedido": pedido.tipo.name,
						"nome": pedido.pedinte.user.username,
						"tipo_pedinte": 'Empresa',
						"stand": pedido.pedinte.usuario_empresa.stand,
						"observacao": pedido.observacao,
						"pk": pedido.pk
					})
			return JsonResponse(dados, safe=False)
		else:
			return HttpResponse("Você não tem acesso a essa página")

class DeletarPedido(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo == 1 or request.user.usuario.cargo == 2:
			pk=request.GET.get("pk")
			print(Pedido.objects.filter(pk=pk).count())
			if Pedido.objects.filter(pk=pk).count() == 0:
				return HttpResponse("Pedido invalido", status=400)
			pedido = Pedido.objects.get(pk=pk)
			pedido.delete()
			data = {
				'deletou': True
			}
			return JsonResponse(data)
		else:
			return render(request, 'erro_403.html')


class Pedidos(View):
	def get(self, request, *args, **kwargs):
		cargo = request.user.usuario.cargo 
		if cargo != 0 and cargo != 3:
			return render(request, 'erro_403.html')
		current_user = request.user
		empresa = None
		if cargo == 0:
			empresa = current_user.usuario.usuario_empresa.organizador_resp
			tipos_de_pedidos = Type.objects.filter(caravaneiro=False)
			template_base = 'base_menus_empresa.html'
		if cargo == 3:
			tipos_de_pedidos = Type.objects.filter(caravaneiro=True)
			template_base = 'base_menus_caravaneiro.html'
		return render(request, 'pedir.html', {'tipos':tipos_de_pedidos, 'organizador': empresa, 'template_base': template_base})


	def post(self, request, *args, **kwargs):
		tipos_de_pedidos = Type.objects.all()
		form = PedidosForm(request.POST)
		current_user = request.user
		organizador = current_user.usuario.usuario_empresa.organizador_resp
		pedido = Pedido.objects.create(tipo = Type.objects.get(pk=form.data['tipo_de_pedido']), 
										observacao = form.data['obs'],
										pedinte = current_user.usuario,
										organizador = current_user.usuario.usuario_empresa.organizador_resp)
		messages.success(request, 'Form submission successful')
		pedido.save()
		return render(request, 'pedir.html', {'tipos':tipos_de_pedidos, 'form': form, 'organizador': organizador})



class CriarPedido(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo == 2:
			form = TypeForm()
			return render(request, 'criar_pedidos.html', {'form': form, 'messages': messages, 'post': False})
		else:
			return render(request, 'erro_403.html')

	def post(self, request, *args, **kwargs):
		form = TypeForm(request.POST, request.FILES)
		print(form)
		enviou = False
		if form.is_valid():
			pedido = form.save()
			enviou = True
			messages.success(request, "Pedido criado com sucesso")
		return render(request, 'criar_pedidos.html', {'form' : form, 'messages': messages, 'post': True, 'enviou': enviou})

class DefinirHorarios(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo != 2:
			return render(request, 'erro_403.html')
		form = ValoresMassagemForm()
		return render(request, 'definir_horarios.html', {'form': form})
	
	def post(self, request, *args, **kwargs):
		form = ValoresMassagemForm(request.POST)
		if form.is_valid:
			valores = ValoresEstaticos.objects.all()[0]
			valores.horario_massagem_inicio = form.data['horario_massagem_inicio']
			valores.horario_massagem_fim = form.data['horario_massagem_fim']
			valores.intervalo_massagem = form.data['intervalo_massagem']
			valores.n_salas = form.data['n_salas']
			valores.save()
		return render(request, 'definir_horarios.html', {'form': form})


def CriarLista(inicio, fim, intervalo):
	lista = []
	element = inicio
	while element <= fim:
		lista.append(element)
		element += intervalo
	return lista
