from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
app_name = 'chat'

urlpatterns = [

	url(r'^carregar-mensagens/$', login_required(CarregarMensagens.as_view()), name='Carregar Mensagens'),
]