

from django.conf.urls import url, include

#app import
from .views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

app_name = 'usuarios'

urlpatterns = [

    url(r'^admin/$', login_required(DashboardAdmin.as_view()), name='Dashboard de admin'),
    url(r'^organizador/$', login_required(DashboardOrganizador.as_view()), name='Dashboard de organizador'),
    url(r'^empresa/$', login_required(DashboardEmpresa.as_view()), name='Dashboard de empresa'),
    url(r'^caravaneiro/$', login_required(DashboardCaravaneiro.as_view()), name='Dashboard de caravaneiro'),
    url(r'^redirecionar/$', login_required(Redirecionar.as_view()), name='Redirecionar'),
    url(r'^cadastro-empresa/$', login_required(CadastroEmpresa.as_view()), name = 'Cadastro de empresa'),
    url(r'^cadastro-organizador/$', login_required(CadastroOrganizador.as_view()), name = 'Cadastro de organizador'),
    url(r'^logout/$', login_required(LogoutView.as_view(template_name='logout.html')), name = 'Logout'),
    url(r'^editar-empresa/(?P<pk>\d+)$', login_required(EditarEmpresa.as_view()), name = 'EditarEmpresa'),
    url(r'^perfil-organizador/$', login_required(PerfilOrganizador.as_view()), name = 'Perfil organizador'),
    url(r'^minhas-empresas/$', login_required(MinhasEmpresas.as_view()), name = 'Minhas empresas'),
    url(r'^todos-organizadores/$', login_required(TodosOrganizadores.as_view()), name = 'Index Organizadores'),
    url(r'^perfil-empresa/$', login_required(PerfilEmpresa.as_view()), name = 'Perfil empresa'),
    url(r'^cadastro-caravaneiro/$', login_required(CadastroCaravaneiro.as_view()), name= 'Cadastro caravaneiro'),
    url(r'^deletar-organizador/$', DeletarOrganizador.as_view(), name='Deletar'),
]