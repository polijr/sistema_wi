from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
app_name = 'chat'

urlpatterns = [

	url(r'^criar-mensagem/$', login_required(CriarMensagem.as_view()), name='Criar Mensagens'),
	url(r'^carregar-mensagens/$', login_required(CarregarMensagens.as_view()), name='Carregar Mensagens'),
	url(r'^recebeu-mensagem/$', login_required(RecebeuMensagem.as_view()), name='Recebeu Mensagem')
]