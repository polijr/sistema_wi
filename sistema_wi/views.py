
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from .models import dataFeed
from .forms import DataForm
from sistema_wi.forms import ValoresEstaticosForm
from django.http import HttpResponseRedirect
from sistema_wi.models import ValoresEstaticos


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
        form = ValoresEstaticosForm(request.POST)
        variaveis = ValoresEstaticos.objects.all()[0]
        print (form)
        if form.is_valid():
            variaveis.ano_wi = request.POST["ano_wi"]
            variaveis.nome_wifi = request.POST["nome_wifi"]
            variaveis.senha_wifi = request.POST["senha_wifi"]
            variaveis.data_de_inicio = request.POST["data_de_inicio"]
            variaveis.mapa_wi = request.POST["mapa_wi"]
            variaveis.calendario_wi = request.POST["calendario_wi"]
            variaveis.save()
            return HttpResponseRedirect('/usuarios/admin')
        return render(request, "valores_estaticos.html", {'variaveis': variaveis})       

class SeleçãoWI(View):
    def get(self, request, *args, **kwargs):
        return render(request, "seleção_wi.html")