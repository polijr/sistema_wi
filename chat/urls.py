from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

app_name = 'chat'

urlpatterns = [

	url(r'^criar-mensagem/$', csrf_exempt(login_required(CriarMensagem.as_view())), name='Criar Mensagens'),
	url(r'^carregar-mensagens/(?P<pk>\d+)$', csrf_exempt(login_required(CarregarMensagens.as_view())), name='Carregar Mensagens'),
	url(r'^mensagens-nao-vistas/(?P<pk>\d+)$', csrf_exempt(login_required(MensagensNaoVisualizadas.as_view())), name='Carregar Mensagens'),
	url(r'^recebeu-mensagem/$',csrf_exempt(login_required(RecebeuMensagem.as_view())), name='Recebeu Mensagem'),
	url(r'^chat/(?P<pk>\d+)$',csrf_exempt( login_required(Chat.as_view())), name='Chat')
]