from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import Documento
from .forms import DocumentoForm
from django.contrib import messages

class EnviarDocumento(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo == 0:
			form = DocumentoForm()
			return render(request, 'enviar_documentos.html', {'form': form, 'messages': messages, 'post': False})
		else:
			return HttpResponse('Você não tem acesso a essa página')

	def post(self, request, *args, **kwargs):
		form = DocumentoForm(request.POST, request.FILES)
		enviou = False
		if form.is_valid():
			documento = form.save(empresa=request.user.usuario.usuario_empresa)
			enviou = True
		messages.success(request, "Documento submetido com sucesso")
		return render(request, 'enviar_documentos.html', {form: 'form', 'messages': messages, 'post': True, 'enviou': enviou})




# class VerDocumento(View):
# 	def get(self, request, *args, **kwargs):
# 		current_user = request.user
# 		documento = current_user.usuario.usuario_organizador.empresa_set.all()

