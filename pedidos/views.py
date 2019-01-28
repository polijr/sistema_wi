from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

class CarregarAjax(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo == 1:
			dados = []
			for pedido in Pedido.objects.all().order_by("data"):
				dados.append({
					"tipo-pedido": pedido.tipo.name,
					"empresa": pedido.pedinte.usuario.user.username,
					"stand": pedido.pedinte.stand,
					"observacao": pedido.observacao,
					"pk": pedido.pk
				})
			return JsonResponse(dict(genres=dados))
		else:
			return HttpResponse("Você não tem acesso a essa página")

class DeletarAjax(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo == 1:
			pedido = Pedido.objects.get(pk=request.GET.get("pk"))
			pedido.delete()
			data = {
				'deletou': True
			}
			return JsonResponse(data)
		else:
			return HttpResponse("Você não tem acesso a essa página")
