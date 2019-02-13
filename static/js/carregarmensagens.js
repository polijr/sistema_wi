function CarregarMensagens(pk) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", 'chat/carregaemensagens/?pk='+ pk + '&primeira_vez=True');
	xhr.addEventListener("load", function() {
		var mensagens = JSON.parse(this.responseText);
		mensagens.mensagens_recebidas.forEach(MensagensRecebidas);
		mensagens.mensagens_enviadas.forEach(MensagensEnviadas);
	});
	xhr.send();

	setInterval(function() {
		xhr.open("GET", '/chat/carregar-mensagens/?pk=' + pk + '&primeira_vez=False');
		xhr.send();
	}, 3000);
}

function Mensagens() {
	// Algo pra fazer pra todas as mensagens
}

function MensagensRecebidas(mensagem) {
	Mensagens();
	// Algo pra fazer só com as mensagens recebidas
}

function MensagensEnviadas(mensagem) {
	Mensagens();
	// Algo pra fazer só com as mensagens enviadas
}