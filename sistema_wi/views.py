
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from .models import dataFeed, LinkFeed, CheckFeed
from .forms import DataForm, LinkForm
from sistema_wi.forms import ValoresEstaticosForm
from django.http import HttpResponseRedirect
from sistema_wi.models import ValoresEstaticos
from django.contrib import messages
import json

def handler404(request, exception, template_name="erro_404.html"):
    response = render_to_response("erro_404.html")
    response.status_code = 404
    return response

def handler403(request, exception, template_name="erro_403.html"):
    response = render_to_response("erro_403.html")
    response.status_code = 403
    return response

def handler500(request, exception, template_name="erro_500.html"):
    response = render_to_response("erro_500.html")
    response.status_code = 500
    return response

def handler400(request, exception, template_name="erro_400.html"):
    response = render_to_response("erro_400.html")
    response.status_code = 400
    return response



class DefinirDataFeed(View):
 def get(self, request, *args, **kwargs):
            if request.user.usuario.cargo == 2:
                  form = DataForm()
                  return render(request, 'definir_data_feed.html', {'form': form, 'post': False})
			
 def post(self, request, *args, **kwargs):
            form = DataForm(request.POST)
            if form.is_valid():
                  form.save()
            return render(request, 'definir_data_feed.html', {'form' : form, 'post': True})


class ValoresSistema(View):
    def get(self, request, *args, **kwargs):
        return render(request, "valores_estaticos.html")
    
    def post(self, request, *args, **kwargs):
        form = ValoresEstaticosForm(request.POST, request.FILES)
        variaveis = ValoresEstaticos.objects.all()[0]
        if form.is_valid():
            variaveis.ano_wi = request.POST.get('ano_wi', False)
            variaveis.nome_wifi = request.POST.get('nome_wifi', False)
            variaveis.senha_wifi = request.POST.get('senha_wifi', False)
            variaveis.data_de_inicio = request.POST.get('data_de_inicio', False)
            if request.FILES.get('calendario_wi', False)!=False:
                variaveis.calendario_wi = request.FILES.get('calendario_wi', False)
            if request.FILES.get('mapa_wi', False) != False:
                variaveis.mapa_wi = request.FILES.get('mapa_wi', False)
            variaveis.save()
            return HttpResponseRedirect('/usuarios/admin')
        return render(request, "valores_estaticos.html", {'variaveis': variaveis})       

class SeleçãoWI(View):
    def get(self, request, *args, **kwargs):
        return render(request, "seleção_wi.html")



class CriarLink(View):
	def get(self, request, *args, **kwargs):
		if request.user.usuario.cargo == 2:
			form = LinkForm()
			return render(request, 'criar_link.html', {'form': form})
		else:
			return render(request, 'erro_403.html')

	def post(self, request, *args, **kwargs):
		form = LinkForm(request.POST, request.FILES)
		enviou = False
		if form.is_valid():
			form.save()
			messages.success(request, "Link criado com sucesso")
		return render(request, 'criar_link.html', {'form': form})



class ListaFeedbackAdm(View):
 def get(self, request, *args, **kwargs):
            if request.user.usuario.cargo == 2:
                lista = LinkFeed.objects.all()
                return render(request, 'lista_feedbacks_adm.html', {'lista': lista})
            
            else:
                return render(request, "erro_403.html")

class DeletarLink(View):
	def get(self, request, *args, **kwargs):
		if not (request.user.usuario.cargo == 2 and LinkFeed.objects.filter(pk=request.GET['pk']).exists()):
			return render(request, 'erro_403.html')
		link = LinkFeed.objects.get(pk=request.GET['pk'])
		link.delete()
		return JsonResponse({'deletou': True})



class EditarLink(View):
	def get(self, request, pk, *args, **kwargs):
		if not (request.user.usuario.cargo == 2 and LinkFeed.objects.filter(pk=pk).exists()):
			return render(request, 'erro_403.html')
		form = LinkForm()
		objeto = LinkFeed.objects.get(pk=pk)
		return render(request, 'editar_link.html', {'form': form, 'objeto': objeto })

	def post(self, request, pk, *args, **kwargs):
		objeto = LinkFeed.objects.get(pk=pk)
		objeto.nome = request.POST['nome']
		objeto.link = request.POST['link']
		objeto.save()
		return HttpResponseRedirect('/lista-feedback-admin')



class ListaFeedback(View):
    def get(self, request, *args, **kwargs):
            if request.user.usuario.cargo == 0:
                lista = list(LinkFeed.objects.all().values())
                for i,el  in enumerate(LinkFeed.objects.all()):
                    try:
                        objs = CheckFeed.objects.filter(feedback=el, empresa=request.user.usuario.usuario_empresa)
                        lista[i]["toggle_id"]=objs[0].pk
                        lista[i]["toggle_status"]=objs[0].status
                    except:
                        obj = CheckFeed.objects.create(
                            feedback=el,
                            empresa=request.user.usuario.usuario_empresa,
                            status=False
                        )
                        obj.save()
                        lista[i]["toggle_id"]=obj.pk
                        lista[i]["toggle_status"]=obj.status
                return render(request, 'lista_feedbacks.html', {'lista': lista})
            else:
                return render(request, "erro_403.html")

class CheckFeedView(View):
    def post(self, request, *args, **kwargs):
        body= json.loads(request.body.decode('utf-8'))
        if CheckFeed.objects.filter(pk=int(body['pk'])).exists():
            obj = CheckFeed.objects.filter(pk=body['pk'])[0]
            obj.status = body['status']
            obj.save()
            return HttpResponse(status=200)
        return HttpResponse(status=500)


			
