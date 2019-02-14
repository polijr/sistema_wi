from .models import ValoresEstaticos
from usuarios.models import Empresa
import datetime
def add_variable_to_context(request):
    try:
        variaveis = ValoresEstaticos.objects.all()[0]
        dias_pro_workshop = (variaveis.data_de_inicio - datetime.datetime.now().date()).days
        empresageral = Empresa.objects.all()
        return {
        'variaveis':  variaveis,
        'dias_pro_workshop': dias_pro_workshop,
        'empresageral': empresageral
        }
    except:
        print("Sem valores estaticos no sistema")
    return {
        'variaveis':  "Vazio"
    }