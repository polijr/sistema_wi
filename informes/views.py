from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.contrib import messages
from .forms import InformeForm


# Create your views here.
class CriarInfo(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo == 2:
			form = InformeForm()
			return render(request, 'criar_informe.html', {'form': form, 'messages': messages, 'post': False})
		else:
			return HttpResponse('Você não tem acesso a essa página')

	def post(self, request, *args, **kwargs):
		form = InformeForm(request.POST, request.FILES)
		enviou = False
		if form.is_valid():
			informe = form.save()
			enviou = True
			messages.success(request, "Informe criado com sucesso")
		return render(request, 'criar_informe.html', {'form' : form, 'messages': messages, 'post': True, 'enviou': enviou})