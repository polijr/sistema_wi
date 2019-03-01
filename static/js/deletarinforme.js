function Deletar(pk) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", '/informes/deletar-informe?pk=' + pk);
	xhr.addEventListener("load", function() {
		window.location.reload();
	})
	xhr.send();
}