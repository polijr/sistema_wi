var xhr = new XMLHttpRequest();
xhr.open("GET", "/pedidos/carregar-pedidos/");
var pedidos_anteriores = [];
xhr.addEventListener("load", function() {
	var pedidos = JSON.parse(this.responseText);
	if (!ComparaPedidos(pedidos, pedidos_anteriores)) {
		pedidos_anteriores = pedidos;
		var tabela_nova = '';
		for(var i = 0; i < pedidos.length; i++) {
			tabela_nova += '<tr><td class="font-w600">' + pedidos[i].tipo_pedido + '</td><td class="text-center">'+
			'<div class="btn-group"><div class="block-content block-content-full">'+ '<div class="popup">' +
			'<button class="btn btn-success btn-popup" onclick="MostrarPopUp('+ i +')" type = "button">+</button><span class="popuptext">Nome: ' 
			+ pedidos[i].nome;
			if (pedidos[i].tipo_pedinte == 'Caravaneiro')
				tabela_nova += '<br><span style="color: yellow;">Caravaneiro</span>';
			else {
				tabela_nova += '<br><span style="color: red">Empresa</span><br>Stand: ' + pedidos[i].stand;
			}
			tabela_nova += '<br>Observação: '+ pedidos[i].observacao +'</span></div>'+
			'</div><button class="btn btn-xs btn-default" type="button" data-toggle="tooltip" title="Remove Client"'+
			' onclick="Deletar('+ pedidos[i].pk + ')"><i class="fa fa-times"></i></button></div></td></tr>';
		}
		var tabela_atual = document.querySelector(".corpo-pedidos");
		tabela_atual.innerHTML = tabela_nova;
	}
	
});
xhr.send();

setInterval(function() {
	xhr.open("GET", "/pedidos/carregar-pedidos/");
	xhr.send();
}, 3000);

function ComparaPedidos(pedidos, pedidos_anteriores) {
	if(pedidos.length != pedidos_anteriores.length) {
		return false;
	}
	for(var i = 0; i < pedidos.length; i++) {
		if (pedidos[i].pk != pedidos_anteriores[i].pk) {
			return false;
		}
	}
	return true;
}

function MostrarPopUp(index) {
  var popups = document.querySelectorAll(".popuptext");
  var botoes = document.querySelectorAll(".btn-popup");
  for (var i = 0; i < popups.length; i++) {
    if (i == index) {
        if (popups[i].classList.contains("show")) {
            popups[i].classList.remove("show");
            botoes[i].innerHTML = '+';
        }
        else {
            popups[i].classList.add("show");
            botoes[i].innerHTML = '-';
        }
    }
    else if (popups[i].classList.contains("show")) {
        popups[i].classList.remove("show");
        botoes[i].innerHTML = '+'
    }
  }
  var botao = document.querySelectorAll(".btn-popup")[index];
}