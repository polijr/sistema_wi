from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, JsonResponse
from .models import Documento, Empresa
from .forms import DocumentoForm
from django.contrib import messages
from django.db.models.functions import Length
class EnviarDocumento(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo != 0:
			return render(request, 'erro_403.html')
		form = DocumentoForm()
		return render(request, 'enviar_documentos.html', {'form': form, 'messages': messages, 'post': False})
		
			

	def post(self, request, *args, **kwargs):
		form = DocumentoForm(request.POST, request.FILES)
		enviou = False
		if form.is_valid():
			documento = form.save(empresa=request.user.usuario.usuario_empresa)
			enviou = True
		messages.success(request, "Documento submetido com sucesso")
		return render(request, 'enviar_documentos.html', {'form' : form, 'messages': messages, 'post': True, 'enviou': enviou})


class Enviados(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo != 0:
			return render(request, 'erro_403.html')
		arquivos = request.user.usuario.usuario_empresa.arquivo_empresa.all()
		return render(request, 'enviados.html', {'arquivos': arquivos})

class EditarDocumento(View):
	def get(self, request, pk, *args, **kwargs):
		if not (request.user.usuario.cargo == 0 and Documento.objects.filter(pk=pk, empresa=request.user.usuario.usuario_empresa).exists()):
			return render(request, 'erro_403.html')
		form = DocumentoForm()
		documento = Documento.objects.get(pk=pk)
		return render(request, 'editar_documento.html', {'form': form, 'messages': messages, 'documento': documento })

	def post(self, request, pk, *args, **kwargs):
		documento = Documento.objects.get(pk=pk)
		documento.nome = request.POST['nome']
		documento.arquivo = request.FILES['arquivo']
		documento.observacao = request.POST['observacao']
		documento.save()
		return HttpResponseRedirect('/documentos/enviados')

class DeletarDocumento(View):
	def get(self, request, *args, **kwargs):
		if not (request.user.usuario.cargo == 0 and Documento.objects.filter(pk=request.GET['pk'], empresa=request.user.usuario.usuario_empresa).exists()):
			return render(request, 'erro_403.html')
		documento = Documento.objects.get(pk=request.GET['pk'])
		documento.delete()
		return JsonResponse({'deletou': True})
			

class VerDocumento(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo == 1:
			organizador = request.user.usuario.usuario_organizador 
			empresas = organizador.empresa_organizador.all()
			template_base = 'base_menus_organizador.html'
		elif request.user.usuario.cargo == 2:
			empresas = Empresa.objects.all()
			template_base = 'base_menus_admin.html'
		else:
			return render(request, 'erro_403.html')
		return render(request, 'ver_documentos.html', {'empresas':empresas, 'template_base': template_base})

