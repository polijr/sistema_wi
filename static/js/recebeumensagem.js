var marcadores = document.querySelectorAll(".notificacao");

var recebeuMensagemXhr = new XMLHttpRequest();
recebeuMensagemXhr.open("GET", '/chat/recebeu-mensagem/');
recebeuMensagemXhr.addEventListener("load", function() {
	var recebeu = JSON.parse(this.responseText);
	for (var i = 0; i < recebeu.length; i++) {
		if (recebeu[i]) {
			marcadores[i].classList.add("fa-circle");
		}
		else {
			marcadores[i].classList.remove("fa-circle");
		}
	}
});
recebeuMensagemXhr.send();

setInterval( function() {
	recebeuMensagemXhr.open("GET", '/chat/recebeu-mensagem/');
	recebeuMensagemXhr.send();
}, 3000);