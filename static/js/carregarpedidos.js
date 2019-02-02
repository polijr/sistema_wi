var xhr = new XMLHttpRequest();
xhr.open("GET", "/pedidos/carregar-pedidos/");
var pedidos_anteriores = [];
xhr.addEventListener("load", function() {
	var pedidos = JSON.parse(this.responseText);
	if (!ComparaPedidos(pedidos, pedidos_anteriores)) {
		pedidos_anteriores = pedidos;
		var tabela_nova = '';
		for(var i = 0; i < pedidos.length; i++) {
			///tipo de pedido = pedidos[i].tipo_pedido
			///nome da empresa = pedidos[i].empresa
			///stand = pedidos[i].stand
			///observação = pedidos[i].observacao

			tabela_nova += '<tr><td class="font-w600">' + pedidos[i].tipo_pedido + '</td><td class="text-center">'+
			'<div class="btn-group"><div class="block-content block-content-full">'+ '<div class="popup">' +
			'<button class="btn btn-success btn-popup" onclick="MostrarPopUp('+ i +')" type = "button">+</button><span class="popuptext">Empresa: ' 
			+ pedidos[i].empresa + ', Stand: ' + pedidos[i].stand + ', Observação: '+ pedidos[i].observacao +'</span></div>'+
			'</div><button class="btn btn-xs btn-default" type="button" data-toggle="tooltip" title="Remove Client"'+
			' onclick="Deletar('+ pedidos[i].pk + ')"><i class="fa fa-times"></i></button></div></td></tr>';
		}
		var tabela_atual =document.querySelector(".corpo-pedidos");
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