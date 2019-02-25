from django.conf.urls import url, include
from .views import *
from django.contrib.auth.decorators import login_required
app_name = 'pedidos'

urlpatterns = [
	#url(r'^pedir/$', login_required(LogoutView.as_view()), name = 'Pedir'),
	url(r'^carregar-pedidos/$', CarregarPedidos.as_view(), name='Carregar'),
	url(r'^deletar-pedidos/$', DeletarPedido.as_view(), name='Deletar'),
	url(r'^pedidos/$', Pedidos.as_view(), name = 'Pedidos'),
	url(r'^criar-pedidos/$', CriarPedido.as_view(), name = 'criarPedidos'),
	url(r'^definir-horarios/$', login_required(DefinirHorarios.as_view()), name='Definir Horarios')
]