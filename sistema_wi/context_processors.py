from .models import ValoresEstaticos, dataFeed
from usuarios.models import Empresa
from django.shortcuts import render, redirect
import datetime
import random
import math
def add_variable_to_context(request):
    try:
        variaveis = ValoresEstaticos.objects.all()[0]
        dias_pro_workshop = (variaveis.data_de_inicio - datetime.datetime.now().date()).days
        if request.user.usuario.cargo == 1:
            user_organizador = request.user.usuario.usuario_organizador
            empresageral = Empresa.objects.filter(organizador_resp = user_organizador)
            return {
            'variaveis':  variaveis,
            'dias_pro_workshop': dias_pro_workshop,
            'empresageral': empresageral
            }
        else:
            return {
            'variaveis':  variaveis,
            'dias_pro_workshop': dias_pro_workshop
            }
    except:
        print("4")
        pass
    return {
        'variaveis':  "Vazio"
    }


def date_now(request):
    return {'date_now':datetime.date.today()}


def nome_aleatorio(request):
    init = (math.ceil(12 * random.random()))
    num = (init % 6)
    if(num == 0):
        nome = "Barbara"
        sobrenome = "Beltrami"
    if (num == 1):
        nome = "Gabriel"
        sobrenome = "dos Anjos"
    if (num == 2):
        nome = "Eduardo"
        sobrenome = "Motta"
    if (num == 3):
        nome = "Ilton"
        sobrenome = "Andrew"
    if (num == 4):
        nome = "Pedro"
        sobrenome = "Kassardjian"
    if (num == 5):
        nome = "Rafael"
        sobrenome = "Araripe"
    
    return {'nome_aleatorio': nome, 'sobrenome_aleatorio': sobrenome}
