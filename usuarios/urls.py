

from django.conf.urls import url, include

#app import
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'usuarios'

urlpatterns = [

    url(r'^admin/$', login_required(DashboardAdmin.as_view()), name='Dashboard de admin'),
    url(r'^organizador/$', login_required(DashboardOrganizador.as_view()), name='Dashboard de organizador'),
    url(r'^empresa/$', login_required(DashboardEmpresa.as_view()), name='Dashboard de empresa'),
    url(r'^cadastro-empresa/$', login_required(CadastroEmpresa.as_view()), name = 'Cadastro de empresa')
]