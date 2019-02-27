from django.conf.urls import url, include
from .views import *
from django.contrib.auth.decorators import login_required
app_name = 'pedidos'

urlpatterns = [
	#url(r'^pedir/$', login_required(LogoutView.as_view()), name = 'Pedir'),
	url(r'^carregar-pedidos/$', CarregarPedidos.as_view(), name='Carregar'),
	url(r'^deletar-pedidos/$', DeletarPedido.as_view(), name='Deletar'),
	url(r'^pedidos/$', Pedidos.as_view(), name = 'Pedidos'),
	url(r'^tipos-de-pedidos/$', TiposDePedidos.as_view(), name = 'Tipos de Pedidos'),
	url(r'^editar-tipo/(?P<pk>\d+)$', EditarTipo.as_view(), name = 'Editar Tipo'),
	url(r'^deletar-tipo/(?P<pk>\d+)$', DeletarTipo.as_view(), name = 'Deletar Tipo'),
	url(r'^criar-pedidos/$', CriarPedido.as_view(), name = 'criarPedidos'),
	url(r'^agendar-massagem/$', FazerAgendamento.as_view(), name = 'agendarMassagem'),
	url(r'^definir-horarios/$', login_required(DefinirHorarios.as_view()), name='Definir Horarios'),
	url(r'^agendamentos/$', login_required(Agendamentos.as_view()), name='Deletar Agendamentos'),
	url(r'^deletar-agendamentos/$', login_required(DeletarAgendamentos.as_view()), name='Deletar Agendamentos'),

]