from .models import ValoresEstaticos
import datetime
def add_variable_to_context(request):
    try:
        variaveis = ValoresEstaticos.objects.all()[0]
        dias_pro_workshop = (variaveis.data_de_inicio - datetime.datetime.now().date()).days
        return {
        'variaveis':  variaveis,
        'dias_pro_workshop': dias_pro_workshop
        }
    except:
        print("Sem valores estaticos no sistema")
    return {
        'variaveis':  "Vazio"
    }