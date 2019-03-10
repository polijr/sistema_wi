from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
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
			pk  = request.GET["pk"]
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
		form = PedidosForm(request.POST)
		current_user = request.user
		empresa = None
		messages.success(request, 'Form submission successful')
		if request.user.usuario.cargo == 0:
			pedido = Pedido.objects.create(tipo = Type.objects.get(pk=form.data['tipo_de_pedido']), 
								observacao = form.data['obs'],
								pedinte = current_user.usuario,
								organizador = current_user.usuario.usuario_empresa.organizador_resp)
			empresa = current_user.usuario.usuario_empresa.organizador_resp
			tipos_de_pedidos = Type.objects.filter(caravaneiro=False)
			pedido.save()
			template_base = 'base_menus_empresa.html'
		else:
			pedido = Pedido.objects.create(tipo = Type.objects.get(pk=form.data['tipo_de_pedido']), 
								observacao = form.data['obs'],
								pedinte = current_user.usuario,
								organizador = None)
			tipos_de_pedidos = Type.objects.filter(caravaneiro=True)
			pedido.save()
			template_base = 'base_menus_caravaneiro.html'
			
		return render(request, 'pedir.html', {'tipos':tipos_de_pedidos, 'form': form, 'organizador': empresa, 'template_base': template_base})



class CriarPedido(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo == 2:
			form = TypeForm()
			return render(request, 'criar_pedidos.html', {'form': form, 'post': False})
		else:
			return render(request, 'erro_403.html')

	def post(self, request, *args, **kwargs):
		form = TypeForm(request.POST, request.FILES)
		print(form)
		enviou = False
		if form.is_valid():
			tipo=Type.objects.create(name=request.POST["name"], caravaneiro=request.POST["caravaneiro"])
			tipo.save()
			enviou = True
			messages.success(request, "Pedido criado com sucesso")
		return render(request, 'criar_pedidos.html', {'form' : form, 'post': True, 'enviou': enviou})


class TiposDePedidos(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo == 2:
			tipos = Type.objects.all()
			return render(request, 'tipos_de_pedidos.html', {'tipos': tipos})
		return render(request, 'erro_403.html')


class EditarTipo(View):
	def get(self, request, pk, *args, **kwargs):
		if request.user.usuario.cargo == 2:
			tipo = Type.objects.get(pk=pk)
			return render(request, 'editar_tipo.html', {'tipo': tipo})
		else:
			return render(request, 'erro_403.html')

	def post(self, request, pk, *args, **kwargs):
		request.POST._mutable = True
		request.POST['pk'] = pk
		form = TypeForm(request.POST)
		if form.is_valid():
			tipo = Type.objects.get(pk=pk)
			tipo.name = request.POST["name"]
			tipo.caravaneiro = request.POST["caravaneiro"]
			tipo.save()
			messages.success(request, 'Pedido editado com sucesso')
			return redirect('/pedidos/tipos-de-pedidos')
		tipo = Type.objects.get(pk=pk)
		return render(request, 'editar_tipo.html', {'form': form, 'tipo': tipo})


class DeletarTipo(View):
	def get(self, request, pk, *args, **kwargs):
		if request.user.usuario.cargo == 2:
			tipo = Type.objects.get(pk=pk)
			return render(request, 'deletar_tipo.html', {'tipo': tipo})
		else:
			return render(request, 'erro_403.html')

	def post(self, request, pk, *args, **kwargs):
		if request.user.usuario.cargo == 2:
			request.POST._mutable = True
			request.POST['pk'] = pk
			tipo = Type.objects.get(pk=pk)
			form = TypeForm(request.POST)
			print(form)
			if form.is_valid():
				tipo.delete()
				messages.success(request, "Tipo de pedido deletado com sucesso!")
			return redirect("../tipos-de-pedidos")
		else:
			return render(request, 'erro_403.html')



class FazerAgendamento(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo == 0 or request.user.usuario.cargo == 2:
			salas = CriarListaSalas(ValoresEstaticos.objects.all()[0].n_salas)
			horarios = CriarLista(ValoresEstaticos.objects.all()[0].horario_massagem_inicio, 
				ValoresEstaticos.objects.all()[0].horario_massagem_fim,
				 ValoresEstaticos.objects.all()[0].intervalo_massagem,
				 salas)
			if request.user.usuario.cargo == 0:
				template_base = 'base_menus_empresa.html'
			else:
				template_base = 'base_menus_admin.html'
			return render(request, 'realizar_agendamento.html', {'salas': salas, 'horarios':horarios, 'template_base': template_base})
		else:
			return render(request, 'erro_403.html')

	def post(self, request, *args, **kwargs):
		if not Agendamento.objects.filter(horario=request.POST["horario"], sala=request.POST["sala"]).exists():
			reserva = Agendamento.objects.create(horario=request.POST["horario"], cliente=request.user.usuario, sala=request.POST["sala"])
			reserva.save()
			messages.success(request, "Horário reservado com sucesso!")
		if request.user.usuario.cargo == 0:
			template_base = 'base_menus_empresa.html'
		else:
			template_base = 'base_menus_admin.html'
		salas = CriarListaSalas(ValoresEstaticos.objects.all()[0].n_salas)
		horarios = CriarLista(ValoresEstaticos.objects.all()[0].horario_massagem_inicio, 
			ValoresEstaticos.objects.all()[0].horario_massagem_fim,
			ValoresEstaticos.objects.all()[0].intervalo_massagem,
			salas)
		return render(request, 'realizar_agendamento.html', {'salas': salas, 'horarios':horarios, 'template_base': template_base})


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


class Agendamentos(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo == 2:
			template_base = 'base_menus_admin.html'
			agendamentos = Agendamento.objects.all()
			return render(request, 'agendamentos.html', {'agendamentos': agendamentos, 'template_base': template_base})
		elif request.user.usuario.cargo == 0:
			template_base = 'base_menus_empresa.html'
			agendamentos = Agendamento.objects.filter(cliente=request.user.usuario)
			return render(request, 'agendamentos.html', {'agendamentos': agendamentos, 'template_base': template_base})
		else:
			return render(request, 'erro_403.html')


class DeletarAgendamento(View):
	def get(self, request, pk, *args, **kwargs):
		if request.user.usuario.cargo == 2 or request.user.usuario.cargo == 0:
			agendamento = Agendamento.objects.get(pk=pk)
			if request.user.usuario.cargo == 0:
				template_base = 'base_menus_empresa.html'
			else:
				template_base = 'base_menus_admin.html'
			return render(request, 'deletar_agendamento.html', {'agendamento': agendamento, 'template_base': template_base})
		else:
			return render(request, 'erro_403.html')

	def post(self, request, pk, *args, **kwargs):
		if request.user.usuario.cargo == 2 or request.user.usuario.cargo == 0:
			request.POST._mutable = True
			request.POST['pk'] = pk
			agendamento = Agendamento.objects.get(pk=pk)
			agendamento.delete()
			messages.success(request, "Agendamento cancelado com sucesso!")
			return redirect("../agendamentos")
		else:
			return render(request, 'erro_403.html')


class DeletarAgendamentos(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo == 2 or request.user.usuario.cargo == 0:
			if request.user.usuario.cargo == 2:
				template_base = 'base_menus_admin.html'
			if request.user.usuario.cargo == 0:
				template_base = 'base_menus_empresa.html'
			return render(request, 'deletar_agendamentos.html', {'template_base': template_base})
		else:
			return render(request, 'erro_403.html')

	def post(self, request, *args, **kwargs):
		request.POST._mutable = True
		if request.user.usuario.cargo == 2 or request.user.usuario.cargo == 0:
			if request.user.usuario.cargo == 2:
				agendamentos = Agendamento.objects.all()
			if request.user.usuario.cargo == 0:
				agendamentos = Agendamento.objects.filter(cliente=request.user.usuario)
			for agendamento in agendamentos:
				agendamento.delete()
			messages.success(request, "Todos agendamentos deletados com sucesso!")
			return redirect("/pedidos/agendamentos")
		else:
			return render(request, 'erro_403.html')

class VerMassagens(View):
	def get(self, request, *args, **kwargs):
		variaveis = ValoresEstaticos.objects.all()[0]
		salas = CriarListaSalas(ValoresEstaticos.objects.all()[0].n_salas)
		agendamentos = Agendamento.objects.all()
		salas_preenchidas=[]
		for agendamento in agendamentos:
			if agendamento.sala not in salas_preenchidas:
				salas_preenchidas.append(agendamento.sala)
		print(salas_preenchidas)
		return render(request, 'massagista.html', {"variaveis":variaveis,"salas":salas, "agendamentos":agendamentos, "salas_com_horario":salas_preenchidas})



def CriarLista(inicio, fim, intervalo, salas):
	lista = []
	for sala in salas:
		dia = datetime.datetime.now().date()
		hora = inicio
		element = datetime.datetime.combine(dia, hora);
		delta = datetime.timedelta(minutes=intervalo)
		while element.time() <= fim:
			lista.append({'sala': sala, 
				'datetime': element.strftime('%Y-%m-%d %H:%M:%S'),
				'time': element.time(), 
				'reservado': Agendamento.objects.filter(horario=element, sala=sala).exists()})
			element += delta
	return lista


def CriarListaSalas(num_salas):
	lista = []
	i = 1
	while i <= num_salas:
		lista.append("Sala %d" %i)
		i = i + 1
	return lista