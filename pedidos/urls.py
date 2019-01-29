

from django.conf.urls import url, include
from django.conf.urls import url
from .models import *
from .views import *

#app import
from .views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

app_name = 'pedidos'

urlpatterns = [
	url(r'^pedir/$', login_required(LogoutView.as_view(template_name='pedir.html')), name = 'Pedir'),
	url(r'^carregar_ajax/$', CarregarAjax.as_view(), name='Carregar'),
	url(r'^deletar_ajax/$', DeletarAjax.as_view(), name='Deletar'),
]