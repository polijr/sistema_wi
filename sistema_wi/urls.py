"""sistema wi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView
from .views import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import usuarios.views
import usuarios.urls
import pedidos.urls
import documentos.urls
import informes.urls
import chat.urls
import sistema_wi.views
app_name = 'sistema_wi'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True)),
    url(r'^recuperar_senha/$', usuarios.views.EsqueciMinhaSenha.as_view()),
    url(r'^nova-senha/(?P<chave>\w+)$', usuarios.views.NovaSenha.as_view()),
	url(r'^usuarios/', include((usuarios.urls, "usuarios"), namespace='usuarios')),
    url(r'^pedidos/', include((pedidos.urls, "pedidos"), namespace='pedidos')),
    url(r'^documentos/', include((documentos.urls, "documentos"), namespace='documentos')),
    url(r'^informes/', include((informes.urls, "informes"), namespace='informes')),
    url(r'^chat/', include((chat.urls, "chat"), namespace='chat')),
    url(r'^definir_feed/$', DefinirDataFeed.as_view()),
    url(r'^valores-sistema/$', sistema_wi.views.ValoresSistema.as_view()),
    url(r'^seleção-wi/$', sistema_wi.views.SeleçãoWI.as_view()),
    url(r'^criar-link/$', CriarLink.as_view()),
    url(r'^lista-feedback-admin/$', ListaFeedbackAdm.as_view()),
    url(r'^editar-link/(?P<pk>\d+)$', login_required(EditarLink.as_view()), name='Editar Link'),
    url(r'^feedbacks/$', ListaFeedback.as_view()),
    url(r'^check-feedback/$', csrf_exempt(login_required(CheckFeedView.as_view())), name='feed_check'),
    url(r'^deletar-link/$', login_required(DeletarLink.as_view()), name='Deletar Link'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'sistema_wi.views.handler404'
#handler500 = 'sistema_wi.views.handler500'
handler403 = 'sistema_wi.views.handler403'
handler400 = 'sistema_wi.views.handler400'
