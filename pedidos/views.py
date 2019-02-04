from django.shortcuts import render
from django.views.generic import View
from .models import Type, Pedido
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import PedidosForm
from django.contrib import messages
import json

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
			return HttpResponse("Você não tem acesso a essa página", status=401)


class Pedidos(View):
	def get(self, request, *args, **kwargs):
		tipos_de_pedidos = Type.objects.all()
		current_user = request.user
		empresa = current_user.usuario.usuario_empresa.organizador_resp
		return render(request, 'pedir.html', {'tipos':tipos_de_pedidos, 'organizador': empresa})


	def post(self, request, *args, **kwargs):
		tipos_de_pedidos = Type.objects.all()
		form = PedidosForm(request.POST)
		current_user = request.user
		organizador = current_user.usuario.usuario_empresa.organizador_resp
		pedido = Pedido.objects.create(tipo = Type.objects.get(pk=form.data['tipo_de_pedido']), 
										observacao = form.data['obs'],
										pedinte = current_user.usuario.usuario_empresa,
										organizador = current_user.usuario.usuario_empresa.organizador_resp)
		messages.success(request, 'Form submission successful')
		pedido.save()
		return render(request, 'pedir.html', {'tipos':tipos_de_pedidos, 'form': form, 'organizador': organizador})
