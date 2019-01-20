

from django.conf.urls import url, include

#app import
from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'usuarios'

urlpatterns = [

    url(r'^admin/$', login_required(dashboard_admin), name='Dashboard de admin'),
    url(r'^organizador/$', login_required(dashboard_organizador), name='Dashboard de organizador'),
    url(r'^empresa/$', login_required(dashboard_empresa), name='Dashboard de empresa'),
]