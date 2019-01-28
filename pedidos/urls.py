from django.conf.urls import url
from .models import *
from .views import *

urlpatterns = [

	url(r'^carregar_ajax/$', CarregarAjax.as_view(), name='Carregar'),
	url(r'^deletar_ajax/$', DeletarAjax.as_view(), name='Deletar'),
]