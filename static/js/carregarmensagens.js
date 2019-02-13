var div = document.querySelector()
function CarregarMensagens(pk) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", 'chat/carregaemensagens/?pk='+ pk + '&primeira_vez=Sim');
	xhr.addEventListener("load", function() {
		var mensagens = JSON.parse(this.responseText);
		var mensagens_recebidas = mensagens.mensagens_recebidas;
		var mensagens_enviadas = mensagens.mensagens_enviadas;
		var i = 0;
		var j = 0;
		while (i != mensagens_recebidas.length && j != mensagens_enviadas.length) {
			if (mensagens_recebidas[i].data < mensagens_enviadas[j].data) {
				i++;
				MensagensRecebidas(mensagens_recebidas[i]);
			}
			else {
				j++;
				MensagensEnviadas(mensagens_enviadas[j]);
			}
		}
	});
	xhr.send();

	setInterval(function() {
		xhr.open("GET", '/chat/carregar-mensagens/?pk=' + pk + '&primeira_vez=Nao');
		xhr.send();
	}, 3000);
}

function MensagensRecebidas(mensagem) {
	var div_recebida = '<div class="block block-rounded block-transparent push-15 push-50-r"><div class="block block-content block-content-full' +
	'block-content-mini bg-gray-lighter">' + mensagem.texto + '</div></div>';
	div.innerHTML += div_recebida;
}

function MensagensEnviadas(mensagem) {
	var div_enviada =  '<div class="block block-rounded block-transparent push-15 push-50-r"><div class="block block-content block-content-full' +
	'block-content-mini bg-gray-light">' + mensagem.texto + '</div></div>';
	div.innerHTML += div_enviada;
}