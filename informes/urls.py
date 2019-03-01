from django.conf.urls import url, include
from .views import *
from django.contrib.auth.decorators import login_required
app_name = 'informes'

urlpatterns = [
	#url(r'^pedir/$', login_required(LogoutView.as_view()), name = 'Pedir'),
	url(r'^criar-informe/$', CriarInfo.as_view(), name='CriarInfo'),
	url(r'^lista-informes/$', ListaInformes.as_view(), name='CriarInfo'),
	url(r'^deletar-informe/$', login_required(DeletarInforme.as_view()), name='Deletar Informe'),
	url(r'^editar-informe/(?P<pk>\d+)$', EditarInforme.as_view(), name='Editar Informe'),
]