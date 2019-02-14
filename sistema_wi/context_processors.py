from .models import ValoresEstaticos
from usuarios.models import Empresa
import datetime
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
        print("Sem valores estaticos no sistema")
    return {
        'variaveis':  "Vazio"
    }