from .models import ValoresEstaticos
def add_variable_to_context(request):
    variaveis = ValoresEstaticos.objects.all()[0]
    print(variaveis.nome_wifi)
    return {
        'variaveis':  variaveis
    }