from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import Documento, Empresa
from .forms import DocumentoForm
from django.contrib import messages

class EnviarDocumento(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo == 0:
			form = DocumentoForm()
			return render(request, 'enviar_documentos.html', {'form': form, 'messages': messages, 'post': False})
		else:
			return render(request, 'erro_403.html')

	def post(self, request, *args, **kwargs):
		form = DocumentoForm(request.POST, request.FILES)
		enviou = False
		if form.is_valid():
			documento = form.save(empresa=request.user.usuario.usuario_empresa)
			enviou = True
		messages.success(request, "Documento submetido com sucesso")
		return render(request, 'enviar_documentos.html', {'form' : form, 'messages': messages, 'post': True, 'enviou': enviou})




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

