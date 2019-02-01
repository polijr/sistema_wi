var xhr = new XMLHttpRequest();
xhr.open("GET", "/pedidos/carregar-pedidos/");
xhr.addEventListener("load", function() {
	var pedidos = JSON.parse(this.responseText);
	var tabela_nova = ''
	for(var i = 0; i < pedidos.length; i++) {
		///tipo de pedido = pedidos[i].tipo_pedido
		///nome da empresa = pedidos[i].empresa
		///stand = pedidos[i].stand
		///observação = pedidos[i].observacao

		tabela_nova += '<tr><td class="font-w600">' + pedidos[i].tipo_pedido + '</td><td class="text-center">'+
		'<div class="btn-group"><div class="block-content block-content-full">'+
		'<button class="btn btn-success" data-toggle="popover" title="Detalhes" data-placement="top"'+'data-content="Empresa:'+
		pedidos[i].empresa + ', Stand:' + pedidos[i].stand + ', Observação: ' + pedidos[i].observacao + '" type = "button">+</button>'+
		'</div><button class="btn btn-xs btn-default" type="button" data-toggle="tooltip" title="Remove Client"'+
		' onclick=Deletar('+ pedidos[i].pk + ')><i class="fa fa-times"></i></button></div></td></tr>';
	}

	var tabela_atual=document.querySelector(".corpo-pedidos")
	if(tabela_atual.innerHTML != tabela_nova){
	    tabela_atual.innerHTML = tabela_nova
	}
});
xhr.send();

setInterval(function() {
	xhr.open("GET", "/pedidos/carregar-pedidos/");
	xhr.send();
}, 3000);