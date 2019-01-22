import pandas
import os
from .models import *

def tabelaPreco( transportadora_pk  ):
    transportadora = Transportadora.objects.get(pk=transportadora_pk)
    transportadora_pk = transportadora.pk
    try:
        leAdValorem('1. Planilha de Preços', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('AC', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('AL', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('AP', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('AM', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('BA', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('CE', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('DF', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('ES', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('GO', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('MA', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('MT', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('MS', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('MG', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('PA', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('PB', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('PR', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('PE', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('PI', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('RJ', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('RN', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('RS', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('RO', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('RR', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('SC', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('SP', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('SE', transportadora_pk)
    except:
        pass
    try:
        leTabelaPrecoCC('TO', transportadora_pk)
    except:
        pass
    
def leAdValorem(sheetname, transportadora_pk):
    transportadora = Transportadora.objects.get(pk=transportadora_pk)
    path = os.path.abspath('core/static/media/TabelaPreco/tabelaPreco.xlsx')
    tabela = pandas.read_excel(path, sheet_name=sheetname)
    adValorem = tabela['Ad valorem']
    if adValorem != None:
        transportadora.adValorem = adValorem

def leTabelaPrecoCC( origem, transportadora_pk ): # Na hora de chamar a funcao na view chamar assim: leTabelaPrecoCC('SP')

    transportadora = Transportadora.objects.get(pk=transportadora_pk)
    path = os.path.abspath('core/static/media/TabelaPreco/tabelaPreco.xlsx')
    tabela = pandas.read_excel(path, sheet_name=origem)
    acre_CC = tabela['Estado CC']
    alagoas_CC = tabela['Unnamed: 2']
    amapa_CC = tabela['Unnamed: 3']
    amazonas_CC = tabela['Unnamed: 4']
    bahia_CC = tabela['Unnamed: 5']
    ceara_CC = tabela['Unnamed: 6']
    distritoFederal_CC = tabela['Unnamed: 7']
    espiritoSanto_CC = tabela['Unnamed: 8']
    goias_CC = tabela['Unnamed: 9']
    maranhao_CC = tabela['Unnamed: 10']
    matoGrosso_CC = tabela['Unnamed: 11']
    matoGrossoDoSul_CC = tabela['Unnamed: 12']
    minasGerais_CC = tabela['Unnamed: 13']
    para_CC = tabela['Unnamed: 14']
    paraiba_CC = tabela['Unnamed: 15']
    parana_CC = tabela['Unnamed: 16']
    pernambuco_CC = tabela['Unnamed: 17']
    piaui_CC = tabela['Unnamed: 18']
    rioDeJaneiro_CC = tabela['Unnamed: 19']
    rioGrandeDoNorte_CC = tabela['Unnamed: 20']
    rioGrandeDoSul_CC = tabela['Unnamed: 21']
    rondonia_CC = tabela['Unnamed: 22']
    roraima_CC = tabela['Unnamed: 23']
    santaCatarina_CC = tabela['Unnamed: 24']
    saoPaulo_CC = tabela['Unnamed: 25']
    sergipe_CC = tabela['Unnamed: 26']
    tocantins_CC = tabela['Unnamed: 27']
    
    acre_CI = tabela['Estado CI']
    alagoas_CI = tabela['Unnamed: 31']
    amapa_CI = tabela['Unnamed: 32']
    amazonas_CI = tabela['Unnamed: 33']
    bahia_CI = tabela['Unnamed: 34']
    ceara_CI = tabela['Unnamed: 35']
    distritoFederal_CI = tabela['Unnamed: 36']
    espiritoSanto_CI = tabela['Unnamed: 37']
    goias_CI = tabela['Unnamed: 38']
    maranhao_CI = tabela['Unnamed: 39']
    matoGrosso_CI = tabela['Unnamed: 40']
    matoGrossoDoSul_CI = tabela['Unnamed: 41']
    minasGerais_CI = tabela['Unnamed: 42']
    para_CI = tabela['Unnamed: 43']
    paraiba_CI = tabela['Unnamed: 44']
    parana_CI = tabela['Unnamed: 45']
    pernambuco_CI = tabela['Unnamed: 46']
    piaui_CI = tabela['Unnamed: 47']
    rioDeJaneiro_CI = tabela['Unnamed: 48']
    rioGrandeDoNorte_CI = tabela['Unnamed: 49']
    rioGrandeDoSul_CI = tabela['Unnamed: 50']
    rondonia_CI = tabela['Unnamed: 51']
    roraima_CI = tabela['Unnamed: 52']
    santaCatarina_CI = tabela['Unnamed: 53']
    saoPaulo_CI = tabela['Unnamed: 54']
    sergipe_CI = tabela['Unnamed: 55']
    tocantins_CI = tabela['Unnamed: 56']

    acre_IC = tabela['Estado IC']
    alagoas_IC = tabela['Unnamed: 60']
    amapa_IC = tabela['Unnamed: 61']
    amazonas_IC = tabela['Unnamed: 62']
    bahia_IC = tabela['Unnamed: 63']
    ceara_IC = tabela['Unnamed: 64']
    distritoFederal_IC = tabela['Unnamed: 65']
    espiritoSanto_IC = tabela['Unnamed: 66']
    goias_IC = tabela['Unnamed: 67']
    maranhao_IC = tabela['Unnamed: 68']
    matoGrosso_IC = tabela['Unnamed: 69']
    matoGrossoDoSul_IC = tabela['Unnamed: 70']
    minasGerais_IC = tabela['Unnamed: 71']
    para_IC = tabela['Unnamed: 72']
    paraiba_IC = tabela['Unnamed: 73']
    parana_IC = tabela['Unnamed: 74']
    pernambuco_IC = tabela['Unnamed: 75']
    piaui_IC = tabela['Unnamed: 76']
    rioDeJaneiro_IC = tabela['Unnamed: 77']
    rioGrandeDoNorte_IC = tabela['Unnamed: 78']
    rioGrandeDoSul_IC = tabela['Unnamed: 79']
    rondonia_IC = tabela['Unnamed: 80']
    roraima_IC = tabela['Unnamed: 81']
    santaCatarina_IC = tabela['Unnamed: 82']
    saoPaulo_IC = tabela['Unnamed: 83']
    sergipe_IC = tabela['Unnamed: 84']
    tocantins_IC = tabela['Unnamed: 85']

    acre_II = tabela['Estado II']
    alagoas_II = tabela['Unnamed: 89']
    amapa_II = tabela['Unnamed: 90']
    amazonas_II = tabela['Unnamed: 91']
    bahia_II = tabela['Unnamed: 92']
    ceara_II = tabela['Unnamed: 93']
    distritoFederal_II = tabela['Unnamed: 94']
    espiritoSanto_II = tabela['Unnamed: 95']
    goias_II = tabela['Unnamed: 96']
    maranhao_II = tabela['Unnamed: 97']
    matoGrosso_II = tabela['Unnamed: 98']
    matoGrossoDoSul_II = tabela['Unnamed: 99']
    minasGerais_II = tabela['Unnamed: 100']
    para_II = tabela['Unnamed: 101']
    paraiba_II = tabela['Unnamed: 102']
    parana_II = tabela['Unnamed: 103']
    pernambuco_II = tabela['Unnamed: 104']
    piaui_II = tabela['Unnamed: 105']
    rioDeJaneiro_II = tabela['Unnamed: 106']
    rioGrandeDoNorte_II = tabela['Unnamed: 107']
    rioGrandeDoSul_II = tabela['Unnamed: 108']
    rondonia_II = tabela['Unnamed: 109']
    roraima_II = tabela['Unnamed: 110']
    santaCatarina_II = tabela['Unnamed: 111']
    saoPaulo_II = tabela['Unnamed: 112']
    sergipe_II = tabela['Unnamed: 113']
    tocantins_II = tabela['Unnamed: 114']
    
    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=acre_CC[i], peso=i, estado='AC', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AC_CC'
        valor.save()
        
        valor = Valor.objects.create(valor=acre_CI[i], peso=i, estado='AC', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AC_CI'
        valor.save()
        
        valor = Valor.objects.create(valor=acre_IC[i], peso=i, estado='AC', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AC_IC'
        valor.save()
        
        valor = Valor.objects.create(valor=acre_II[i], peso=i, estado='AC', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AC_II'
        valor.save()
        
        i += 1
    
    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=alagoas_CC[i], peso=i, estado='AL', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AL_CC'
        valor.save()
        
        valor = Valor.objects.create(valor=alagoas_CI[i], peso=i, estado='AL', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AL_CI'
        valor.save()

        valor = Valor.objects.create(valor=alagoas_IC[i], peso=i, estado='AL', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AL_IC'
        valor.save()

        valor = Valor.objects.create(valor=alagoas_II[i], peso=i, estado='AL', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AL_II'
        valor.save()
        
        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=amapa_CC[i], peso=i, estado='AP', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AP_CC'
        valor.save()

        valor = Valor.objects.create(valor=amapa_CI[i], peso=i, estado='AP', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AP_CI'
        valor.save()

        valor = Valor.objects.create(valor=amapa_IC[i], peso=i, estado='AP', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AP_IC'
        valor.save()

        valor = Valor.objects.create(valor=amapa_II[i], peso=i, estado='AP', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AP_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=amazonas_CC[i], peso=i, estado='AM', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AM_CC'
        valor.save()

        valor = Valor.objects.create(valor=amazonas_CI[i], peso=i, estado='AM', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AM_CI'
        valor.save()

        valor = Valor.objects.create(valor=amazonas_IC[i], peso=i, estado='AM', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AM_IC'
        valor.save()

        valor = Valor.objects.create(valor=amazonas_II[i], peso=i, estado='AM', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'AM_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=bahia_CC[i], peso=i, estado='BA', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'BA_CC'
        valor.save()

        valor = Valor.objects.create(valor=bahia_CI[i], peso=i, estado='BA', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'BA_CI'
        valor.save()

        valor = Valor.objects.create(valor=bahia_IC[i], peso=i, estado='BA', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'BA_IC'
        valor.save()

        valor = Valor.objects.create(valor=bahia_II[i], peso=i, estado='BA', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'BA_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=ceara_CC[i], peso=i, estado='CE', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'CE_CC'
        valor.save()

        valor = Valor.objects.create(valor=ceara_CI[i], peso=i, estado='CE', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'CE_CI'
        valor.save()

        valor = Valor.objects.create(valor=ceara_IC[i], peso=i, estado='CE', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'CE_IC'
        valor.save()

        valor = Valor.objects.create(valor=ceara_II[i], peso=i, estado='CE', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'CE_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=distritoFederal_CC[i], peso=i, estado='DF', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'DF_CC'
        valor.save()

        valor = Valor.objects.create(valor=distritoFederal_CI[i], peso=i, estado='DF', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'DF_CI'
        valor.save()

        valor = Valor.objects.create(valor=distritoFederal_IC[i], peso=i, estado='DF', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'DF_IC'
        valor.save()

        valor = Valor.objects.create(valor=distritoFederal_II[i], peso=i, estado='DF', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'DF_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=espiritoSanto_CC[i], peso=i, estado='ES', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'ES_CC'
        valor.save()

        valor = Valor.objects.create(valor=espiritoSanto_CI[i], peso=i, estado='ES', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'ES_CI'
        valor.save()

        valor = Valor.objects.create(valor=espiritoSanto_IC[i], peso=i, estado='ES', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'ES_IC'
        valor.save()

        valor = Valor.objects.create(valor=espiritoSanto_II[i], peso=i, estado='ES', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'ES_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=goias_CC[i], peso=i, estado='GO', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'GO_CC'
        valor.save()

        valor = Valor.objects.create(valor=goias_CI[i], peso=i, estado='GO', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'GO_CI'
        valor.save()

        valor = Valor.objects.create(valor=goias_IC[i], peso=i, estado='GO', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'GO_IC'
        valor.save()

        valor = Valor.objects.create(valor=goias_II[i], peso=i, estado='GO', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'GO_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=maranhao_CC[i], peso=i, estado='MA', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'MA_CC'
        valor.save()

        valor = Valor.objects.create(valor=maranhao_CI[i], peso=i, estado='MA', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'MA_CI'
        valor.save()

        valor = Valor.objects.create(valor=maranhao_IC[i], peso=i, estado='MA', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'MA_IC'
        valor.save()

        valor = Valor.objects.create(valor=maranhao_II[i], peso=i, estado='MA', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'MA_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=matoGrosso_CC[i], peso=i, estado='MG', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'MG_CC'
        valor.save()

        valor = Valor.objects.create(valor=matoGrosso_CI[i], peso=i, estado='MG', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'MG_CI'
        valor.save()

        valor = Valor.objects.create(valor=matoGrosso_IC[i], peso=i, estado='MG', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'MG_IC'
        valor.save()

        valor = Valor.objects.create(valor=matoGrosso_II[i], peso=i, estado='MG', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'MG_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=matoGrossoDoSul_CC[i], peso=i, estado='MS', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'MS_CC'
        valor.save()

        valor = Valor.objects.create(valor=matoGrossoDoSul_CI[i], peso=i, estado='MS', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'MS_CI'
        valor.save()

        valor = Valor.objects.create(valor=matoGrossoDoSul_IC[i], peso=i, estado='MS', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'MS_IC'
        valor.save()

        valor = Valor.objects.create(valor=matoGrossoDoSul_II[i], peso=i, estado='MS', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'MS_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=minasGerais_CC[i], peso=i, estado='MG', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'MG_CC'
        valor.save()

        valor = Valor.objects.create(valor=minasGerais_CI[i], peso=i, estado='MG', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'MG_CI'
        valor.save()

        valor = Valor.objects.create(valor=minasGerais_IC[i], peso=i, estado='MG', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'MG_IC'
        valor.save()

        valor = Valor.objects.create(valor=minasGerais_II[i], peso=i, estado='MG', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            Valor.transportadora.regiaoDeAtuacao.append('MG_II')
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=para_CC[i], peso=i, estado='PA', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PA_CC'
        valor.save()

        valor = Valor.objects.create(valor=para_CI[i], peso=i, estado='PA', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PA_CI'
        valor.save()

        valor = Valor.objects.create(valor=para_IC[i], peso=i, estado='PA', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PA_IC'
        valor.save()

        valor = Valor.objects.create(valor=para_II[i], peso=i, estado='PA', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PA_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=paraiba_CC[i], peso=i, estado='PB', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PB_CC'
        valor.save()

        valor = Valor.objects.create(valor=paraiba_CI[i], peso=i, estado='PB', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PB_CI'
        valor.save()

        valor = Valor.objects.create(valor=paraiba_IC[i], peso=i, estado='PB', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PB_IC'
        valor.save()

        valor = Valor.objects.create(valor=paraiba_II[i], peso=i, estado='PB', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PB_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=parana_CC[i], peso=i, estado='PR', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PR_CC'
        valor.save()

        valor = Valor.objects.create(valor=parana_CI[i], peso=i, estado='PR', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PR_CI'
        valor.save()

        valor = Valor.objects.create(valor=parana_IC[i], peso=i, estado='PR', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PR_IC'
        valor.save()

        valor = Valor.objects.create(valor=parana_II[i], peso=i, estado='PR', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PR_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=pernambuco_CC[i], peso=i, estado='PE', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PE_CC'
        valor.save()

        valor = Valor.objects.create(valor=pernambuco_CI[i], peso=i, estado='PE', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PE_CI'
        valor.save()

        valor = Valor.objects.create(valor=pernambuco_IC[i], peso=i, estado='PE', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PE_IC'
        valor.save()

        valor = Valor.objects.create(valor=pernambuco_II[i], peso=i, estado='PE', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PE_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=piaui_CC[i], peso=i, estado='PI', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PI_CC'
        valor.save()

        valor = Valor.objects.create(valor=piaui_CI[i], peso=i, estado='PI', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PI_CI'
        valor.save()

        valor = Valor.objects.create(valor=piaui_IC[i], peso=i, estado='PI', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PI_IC'
        valor.save()

        valor = Valor.objects.create(valor=piaui_II[i], peso=i, estado='PI', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'PI_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=rioDeJaneiro_CC[i], peso=i, estado='RJ', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RJ_CC'
        valor.save()

        valor = Valor.objects.create(valor=rioDeJaneiro_CI[i], peso=i, estado='RJ', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RJ_CI'
        valor.save()

        valor = Valor.objects.create(valor=rioDeJaneiro_IC[i], peso=i, estado='RJ', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RJ_IC'
        valor.save()

        valor = Valor.objects.create(valor=rioDeJaneiro_II[i], peso=i, estado='RJ', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RJ_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=rioGrandeDoNorte_CC[i], peso=i, estado='RN', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RN_CC'
        valor.save()

        valor = Valor.objects.create(valor=rioGrandeDoNorte_CI[i], peso=i, estado='RN', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RN_CI'
        valor.save()

        valor = Valor.objects.create(valor=rioGrandeDoNorte_IC[i], peso=i, estado='RN', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RN_IC'
        valor.save()

        valor = Valor.objects.create(valor=rioGrandeDoNorte_II[i], peso=i, estado='RN', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RN_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=rioGrandeDoSul_CC[i], peso=i, estado='RS', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RS_CC'
        valor.save()

        valor = Valor.objects.create(valor=rioGrandeDoSul_CI[i], peso=i, estado='RS', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RS_CI'
        valor.save()

        valor = Valor.objects.create(valor=rioGrandeDoSul_IC[i], peso=i, estado='RS', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RS_IC'
        valor.save()

        valor = Valor.objects.create(valor=rioGrandeDoSul_II[i], peso=i, estado='RS', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RS_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=rondonia_CC[i], peso=i, estado='RO', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RO_CC'
        valor.save()

        valor = Valor.objects.create(valor=rondonia_CI[i], peso=i, estado='RO', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RO_CI'
        valor.save()

        valor = Valor.objects.create(valor=rondonia_IC[i], peso=i, estado='RO', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RO_IC'
        valor.save()

        valor = Valor.objects.create(valor=rondonia_II[i], peso=i, estado='RO', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RO_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=roraima_CC[i], peso=i, estado='RR', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RR_CC'
        valor.save()

        valor = Valor.objects.create(valor=roraima_CI[i], peso=i, estado='RR', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RR_CI'
        valor.save()

        valor = Valor.objects.create(valor=roraima_IC[i], peso=i, estado='RR', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RR_IC'
        valor.save()

        valor = Valor.objects.create(valor=roraima_II[i], peso=i, estado='RR', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'RR_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=santaCatarina_CC[i], peso=i, estado='SC', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'SC_CC'
        valor.save()

        valor = Valor.objects.create(valor=santaCatarina_CI[i], peso=i, estado='SC', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'SC_CI'
        valor.save()

        valor = Valor.objects.create(valor=santaCatarina_IC[i], peso=i, estado='SC', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'SC_IC'
        valor.save()

        valor = Valor.objects.create(valor=santaCatarina_II[i], peso=i, estado='SC', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'SC_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=saoPaulo_CC[i], peso=i, estado='SP', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'SP_CC'
        valor.save()

        valor = Valor.objects.create(valor=saoPaulo_CI[i], peso=i, estado='SP', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'SP_CI'
        valor.save()

        valor = Valor.objects.create(valor=saoPaulo_IC[i], peso=i, estado='SP', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'SP_IC'
        valor.save()

        valor = Valor.objects.create(valor=saoPaulo_II[i], peso=i, estado='SP', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'SP_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=sergipe_CC[i], peso=i, estado='SE', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'SE_CC'
        valor.save()

        valor = Valor.objects.create(valor=sergipe_CI[i], peso=i, estado='SE', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'SE_CI'
        valor.save()

        valor = Valor.objects.create(valor=sergipe_IC[i], peso=i, estado='SE', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'SE_IC'
        valor.save()

        valor = Valor.objects.create(valor=sergipe_II[i], peso=i, estado='SE', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'SE_II'
        valor.save()

        i += 1

    i = 1
    while i < 17:
        valor = Valor.objects.create(valor=tocantins_CC[i], peso=i, estado='TO', origem=origem, capital_interior='CC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'TO_CC'
        valor.save()

        valor = Valor.objects.create(valor=tocantins_CI[i], peso=i, estado='TO', origem=origem, capital_interior='CI', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'TO_CI'
        valor.save()

        valor = Valor.objects.create(valor=tocantins_IC[i], peso=i, estado='TO', origem=origem, capital_interior='IC', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'TO_IC'
        valor.save()

        valor = Valor.objects.create(valor=tocantins_II[i], peso=i, estado='TO', origem=origem, capital_interior='II', transportadora=transportadora)
        if valor != None:
            valor.regiaoDeAtuacao = 'TO_II'
        valor.save()

        i += 1
