var marcadores = document.querySelectorAll(".notificacao");

var xhr = new XMLHttpRequest();
xhr.open("GET", '/chat/recebeu-mensagem/');
xhr.addEventListener("load", function() {
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
xhr.send();

setInterval( function() {
	xhr.open("GET", '/chat/recebeu-mensagem/');
	xhr.send();
}, 3000);