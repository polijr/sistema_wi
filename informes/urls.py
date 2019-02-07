from django.conf.urls import url, include
from .views import *
from django.contrib.auth.decorators import login_required
app_name = 'informes'

urlpatterns = [
	#url(r'^pedir/$', login_required(LogoutView.as_view()), name = 'Pedir'),
	url(r'^criar-informe/$', CriarInfo.as_view(), name='CriarInfo'),
]