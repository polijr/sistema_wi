from models import RegraDeNegocio, ProgramacaoTransporte, Pedido, Transportadora
from operator import attrgetter

def ranquear(self, pedido):
    pedido = Pedido.objects.get()
    UFDestino = pedido.UFDestino
    regiaoDestino = pedido.regiaoDestino
    regraDeNegocio = RegraDeNegocio.objects.get(UF=UFDestino, regiao=regiaoDestino)
    todas_transportadoras = Transportadora.objects.all()
    
    min_prazo = min(todas_transportadoras,key=attrgetter('prazo'))
    min_preco = min(todas_transportadoras,key=attrgetter('preco'))
    min_performance = min(todas_transportadoras,key=attrgetter('performance'))
    max_prazo = max(todas_transportadoras,key=attrgetter('prazo'))
    max_preco = max(todas_transportadoras,key=attrgetter('preco'))
    max_performance = max(todas_transportadoras,key=attrgetter('performance'))
    range_prazo = max_prazo - min_prazo
    range_preco = max_preco - min_preco
    range_performance = max_performance - min_performance

    for transportadora in todas_transportadoras:
        transportadora.rankingPrazo = (transportadora.prazo - min_prazo)/range_prazo
        transportadora.rankingPreco = (transportadora.preco - min_preco)/range_preco
        transportadora.rankingPerformance = (transportadora.performance - min_performance)/range_performance
        transportadora.rankingGeral = (transportadora.rankingPrazo * regraDeNegocio.prazo) + (transportadora.rankingPreco * regraDeNegocio.preco) + (transportadora.rankingPerformance * regraDeNegocio.performance)

    todas_transportadoras.sort(key=transportadora.rankingGeral, reverse=True)
