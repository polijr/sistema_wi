from .models import ValoresEstaticos
def add_variable_to_context(request):
    try:
        variaveis = ValoresEstaticos.objects.all()[0]
        return {
        'variaveis':  variaveis
        }
    except:
        print("Sem valores estaticos no sistema")
    return {
        'variaveis':  "Vazio"
    }