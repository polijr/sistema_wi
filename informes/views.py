from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.contrib import messages
from .forms import InformeForm
from django.http import HttpResponseRedirect, JsonResponse


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

class ListaInformes(View):
 def get(self, request, *args, **kwargs):
            if request.user.usuario.cargo == 2:
                lista = Informe.objects.all()
                return render(request, 'lista_informes.html', {'lista': lista})
            
            else:
                return render(request, "erro_403.html")


class DeletarInforme(View):
	def get(self, request, *args, **kwargs):
		if not (request.user.usuario.cargo == 2 and Informe.objects.filter(pk=request.GET['pk']).exists()):
			return render(request, 'erro_403.html')
		informe = Informe.objects.get(pk=request.GET['pk'])
		informe.delete()
		return JsonResponse({'deletou': True})


class EditarInforme(View):
	def get(self, request, pk, *args, **kwargs):
		if not (request.user.usuario.cargo == 2 and Informe.objects.filter(pk=pk).exists()):
			return render(request, 'erro_403.html')
		form = InformeForm()
		objeto = Informe.objects.get(pk=pk)
		return render(request, 'editar_informe.html', {'form': form, 'messages': messages, 'objeto': objeto })

	def post(self, request, pk, *args, **kwargs):
		objeto = Informe.objects.get(pk=pk)
		objeto.titulo = request.POST['titulo']
		objeto.texto = request.POST['texto']
		objeto.save()
		return HttpResponseRedirect('/informes/lista-informes')
