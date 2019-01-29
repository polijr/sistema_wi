var xhr = new XMLHttpRequest();
xhr.open("GET", "/pedidos/carregar_ajax/");
xhr.addEventListener("load", function() {
	var resposta = JSON.parse(this.responseText);
	var pedidos = resposta.genres;
	for(var i = 0; i < pedidos.length; i++) {
		// tipo de pedido = pedidos[i].tipo-pedido
		// nome da empresa = pedidos[i].empresa
		// stand = pedidos[i].stand
		// observação = pedidos[i].observacao
	}
});
xhr.send();

setInterval(function() {
	xhr.open("GET", "/pedidos/carregar_ajax/");
	xhr.send();
}, 3000);