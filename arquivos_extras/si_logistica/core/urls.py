from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.Home.as_view()),
    url(r'^transportadoras/$', views.ListarTransportadoras.as_view(), name='transportadoras_listar'),
    url(r'^transportadora/ver/(?P<transportadora_id>\d+)$', views.VerTransportadora.as_view(), name='transportadora_ver'),
    url(r'^transportadora/cadastrar', views.CadastrarTransportadora.as_view(), name='transportadora_cadastrar'),
    url(r'^transportadora/(?P<pk>\d+)/dados', views.TransportadoraDados.as_view(), name='transportadora_cadastrar_dados'),
    url(r'^transportadora/(?P<pk>\d+)/uploads$', views.TransportadoraUploads.as_view(), name='transportadora_cadastrar_uploads'),
    url(r'^transportadora/(?P<pk>\d+)/uploads_prazo', views.TransportadoraUploadsPrazo.as_view(), name='transportadora_cadastrar_uploads_prazo'),
    url(r'^transportadora/(?P<pk>\d+)/editar', views.EditarTransportadora.as_view(),name='transportadora_editar'),
    url(r'^rastreamento/busca', views.RastreamentoBusca.as_view(), name='rastreamentoBusca'),
    url(r'^rastreamento/periodo', views.RastreamentoPeriodo.as_view(), name='rastreamentoPeriodo'),
    url(r'^pedidos/', views.ListaPedidos.as_view(), name='lista_pedidos'),
    url(r'^pedido/ver/(?P<pk>\d+)', views.VerPedido.as_view(), name='ver_pedido'),
    url(r'^pedido/criar', views.CriarPedido.as_view(), name='criar_pedido'),
    # url(r'^pedidos/alterar/<int:pk>', views.AlteraPedido.as_view(), name='alterar_pedido'),
    # url(r'^pedidos/deletar/<int:pk>', views.DeletaPedido.as_view(), name='deletar_pedido'),
    url(r'^regras/', views.ListaRegraDeNegocio.as_view(), name='lista_regras'),
    # url(r'^regras/ver/<int:pk>', views.VerRegraDeNegocio.as_view(), name='ver_regra'),
    # url(r'^regras/criar', views.CriarRegraDeNegocio.as_view(), name='criar_regra'),
    # url(r'^regras/alterar/<int:pk>', views.AlteraRegraDeNegocio.as_view(), name='alterar_regra'),
    # url(r'^regras/deletar/<int:pk>', views.DeletaRegraDeNegocio.as_view(), name='deletar_regra'),
    url(r'^registros/$', views.ListaRegistro.as_view(), name='registros'),
    url(r'^registros/ver/(?P<pk>\d+)', views.VerRegistro.as_view(), name='ver_registro'),
    url(r'^registros/criar$', views.CriarRegistro.as_view(), name='criar_registro'),
    url(r'^registros/criar-notfis', views.CriarRegistroNotFis.as_view(), name='criar_registro_notfis'),
    url(r'^registros/criar-excel', views.CriarRegistroExcel.as_view(), name='criar_registro_excel'),
    url(r'^registros/programar/(?P<pk>\d+)', views.ProgramarRegistro.as_view(), name='programar_registro'),
    # url(r'^registros/alterar/<int:pk>', views.AlteraRegistro.as_view(), name='alterar_registro'),
    # url(r'^registros/deletar/<int:pk>', views.DeletaRegistro.as_view(), name='deletar_registro'),
    url(r'^programacao/criar', views.CriarProgramacaoTransporte.as_view(), name='criar_programacao'),
    # url(r'^programacao/ver/<int:pk>', views.VerProgramacaoTransporte.as_view(), name='ver_programacao'),
    url(r'^programacao/$', views.ListaProgramacaoTransporte.as_view(), name='programacao_listar'),
    url(r'^exportar/xls/$', views.criar_programacao, name='exportar_programacao'),
    url(r'^exportar/registropadrao/$', views.DownloadExcelPadrao, name="download_registro_padrao"),
    # url(r'^programacao/alterar/<int:pk>', views.AlteraProgramacaoTransporte.as_view(), name='alterar_programacao'),
    # url(r'^programacao/deletar/<int:pk>', views.DeletaProgramacaoTransporte.as_view(), name='deletar_programacao'),
    url(r'^transportadoras/ocoren', views.TransportadoraOCOREN.as_view()),
    url(r'^exportar/tabelaPrazoPadrao/$', views.DownloadTabelaPrazoPadrao, name="download_prazo_padrao"),
    url(r'^exportar/tabelaPrecoPadrao/$', views.DownloadTabelaPrecoPadrao, name="download_preco_padrao"),
    url(r'^relatoriofinanceiro/(?P<tipo_de_relatorio>\w+)/$',views.RelatorioFinanceiro.as_view(),name='relatorio_financeiro'),
    url(r'^exportar_rastreamento/$', views.exportar_rastreamento_views, name="exportar_rastreamento_url"),
    url(r'^relatorio_entrega/(?P<tipo_de_relatorio>\w+)/$', views.GerarRelatorioEntrega.as_view(), name="gerar_relatorio_entrega"),
    url(r'^relatorio_performance/(?P<tipo_de_relatorio>\w+)/$', views.GerarRelatorioPerformance.as_view() , name="gerar_relatorio_performance"),
    url(r'^grafico/entrega/', views.GerarGraficoEntrega.as_view() , name="gerar_grafico_entrega"),
    url(r'^grafico/performance/', views.GerarGraficoPerformance.as_view() , name="gerar_grafico_performance"),
    url(r'^grafico/financeiro/', views.GerarGraficoFinanceiro.as_view() , name="gerar_grafico_financeiro"),
    url(r'^grafico/pendencia/', views.GerarGraficoPendencia.as_view() , name="gerar_grafico_pendencia"),
    url(r'^cadastrarfuncionario/', views.CadastrarFuncionario.as_view() , name="cadastrar_funcionario"),
    url(r'^cadastraradministrador/', views.CadastrarAdministrador.as_view() , name="cadastrar_administrador"),
    url(r'^funcionarios/$', views.ListarFuncionarios.as_view(), name='funcionarios_listar'),
    url(r'^funcionario/ver/(?P<funcionario_id>\d+)$', views.VerFuncionario.as_view(), name='funcionario_ver'),
    url(r'^funcionario/(?P<pk>\d+)/editar', views.EditarFuncionario.as_view(),name='funcionario_editar'),
    url(r'^administradores/$', views.ListarAdministradores.as_view(), name='administradores_listar'),
    url(r'^administrador/ver/(?P<administrador_id>\d+)$', views.VerAdministrador.as_view(), name='administrador_ver'),
    url(r'^administrador/(?P<pk>\d+)/editar', views.EditarAdministrador.as_view(),name='administrador_editar'),
]

