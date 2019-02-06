from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'documentos'

urlpatterns = [

	url(r'^enviar/$', login_required(EnviarDocumento.as_view()), name='Enviar'),
	url(r'^ver-documentos/$', login_required(VerDocumento.as_view()), name='Ver'),
]