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


class Pedidos(View):
    def get(self, request, *args, **kwargs):
        current_user = request.user
        organizador_nome = current_user.usuario.usuario_empresa.organizador_resp.nome
        organizador_sobrenome = current_user.usuario.usuario_empresa.organizador_resp.sobrenome
		organizador_telefone = current_user.usuario.usuario_empresa.organizador_resp.telefone
        return render(request, 'pedir.html', {'organizador_nome': organizador_nome, 'organizador_sobrenome': organizador_sobrenome,
																			 'organizador_telefone': organizador_telefone})


    def post(self, request, *args, **kwargs):
        form = PedidosForm(request.POST)
        pedido = Type.objects.create(tipo_de_pedido = Type.objects.get(pk=form.data['tipo_de_pedido']), 
										obs = form.data['obs'],
										pedinte = current_user.usuario.usuario_empresa,
										organizador_associado = current_user.usuario.usuario_empresa.organizador_resp)
        pedido.save()
		return render(request, 'pedir.html', {'form':form})
        