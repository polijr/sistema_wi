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
			return render(request, 'criar_informe.html', {'form': form})
		else:
			return render(request, 'erro_403.html')

	def post(self, request, *args, **kwargs):
		form = InformeForm(request.POST, request.FILES)
		enviou = False
		if form.is_valid():
			form.save()
			messages.success(request, "Informe criado com sucesso")
		return render(request, 'criar_informe.html', {'form': form})