from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'documentos'

urlpatterns = [

	url(r'^enviar/$', login_required(EnviarDocumento.as_view()), name='Enviar'),
	url(r'^enviados/$', login_required(Enviados.as_view()), name='Enviados'),
	url(r'^editar-documento/(?P<pk>\d+)$', login_required(EditarDocumento.as_view()), name='Editar Documento'),
	url(r'^deletar-documento/$', login_required(DeletarDocumento.as_view()), name='Deletar Documento'),
	url(r'^ver-documentos/$', login_required(VerDocumento.as_view()), name='Ver Documentos'),
	url(r'^ver-nota/$', login_required(VerNota.as_view()), name='Ver Nota'),
	url(r'^enviar-nota/$', login_required(EnviarNota.as_view()), name='Enviar Nota')
]