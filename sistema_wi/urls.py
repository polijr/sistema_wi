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

import usuarios.views
import usuarios.urls
import pedidos.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True)),
    url(r'^recuperar_senha/$', usuarios.views.EsqueciMinhaSenha.as_view()),
	url(r'^usuarios/', include((usuarios.urls, "usuarios"), namespace='usuarios')),
    # url(r'^pedidos/', include((pedidos.urls, "pedidos"), namespace='pedidos')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)