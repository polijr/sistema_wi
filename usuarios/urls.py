

from django.conf.urls import url, include

#app import
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'usuarios'

urlpatterns = [

    url(r'^admin/$', login_required(DashboardAdmin), name='Dashboard de admin'),
    url(r'^organizador/$', login_required(DashboardOrganizador.as_view()), name='Dashboard de organizador'),
    url(r'^empresa/$', login_required(DashboardEmpresa.as_view()), name='Dashboard de empresa'),
]