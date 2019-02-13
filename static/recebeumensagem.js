var xhr = new XMLHttpRequest();
xhr.open("GET", 'chat/recebeu-mensagem/');
xhr.addEventListener("load", function() {
	var resposta = JSON.parse(this.responseText);
	var recebeu = resposta.recebeu;
	if (recebeu) {
		//colocar bolinha
	}
	else {
		//tirar bolinha
	}
});
xhr.send();

setInterval( function() {
	xhr.open("GET", 'chat/recebeu-mensagem/');
	xhr.send();
});