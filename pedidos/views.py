from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.http import JsonResponse

class CarregarAjax(View):
	def get(self, request, *args, **kwargs):
		dados = []
		for pedido in Pedido.objects.all().order_by("data"):
			dados.append({
				"tipo-pedido": pedido.tipo.name,
				"empresa": pedido.pedinte.usuario.user.username,
				"stand": pedido.pedinte.stand,
				"observacao": pedido.observacao
			})
		return JsonResponse(dict(genres=dados))
