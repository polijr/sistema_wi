
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from .models import dataFeed
from .forms import DataForm

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