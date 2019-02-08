

from django.conf.urls import url, include

#app import
from .views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [

    url(r'^admin/$', login_required(DashboardAdmin.as_view()), name='Dashboard de admin'),
    url(r'^organizador/$', login_required(DashboardOrganizador.as_view()), name='Dashboard de organizador'),
    url(r'^empresa/$', login_required(DashboardEmpresa.as_view()), name='Dashboard de empresa'),
    url(r'^redirecionar/$', login_required(Redirecionar.as_view()), name='Redirecionar'),
    url(r'^cadastro-empresa/$', login_required(CadastroEmpresa.as_view()), name = 'Cadastro de empresa'),
    url(r'^cadastro-organizador/$', login_required(CadastroOrganizador.as_view()), name = 'Cadastro de organizador'),
    url(r'^logout/$', login_required(LogoutView.as_view(template_name='logout.html')), name = 'Logout'),
    url(r'^editar-empresa/(?P<pk>\d+)$', login_required(EditarEmpresa.as_view()), name = 'Editar Empresa'),
    url(r'^editar-organizador/(?P<pk>\d+)$', login_required(EditarOrganizador.as_view()), name = 'Editar Organizador'),
    url(r'^perfil-organizador/$', login_required(PerfilOrganizador.as_view()), name = 'Perfil organizador'),
    url(r'^minhas-empresas/$', login_required(MinhasEmpresas.as_view()), name = 'Minhas empresas'),
    url(r'^meus-organizadores/$', login_required(MeusOrganizadores.as_view()), name = 'Meus Organizadores'),
    url(r'^perfil-empresa/$', login_required(PerfilEmpresa.as_view()), name = 'Perfil empresa'),
    url(r'^cadastro-caravaneiro/$', login_required(CadastroCaravaneiro.as_view()), name= 'Cadastro caravaneiro')
]