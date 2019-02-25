function Deletar(pk) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", '/documentos/deletar-nota?pk=' + pk);
	xhr.addEventListener("load", function() {
		window.location.reload();
	})
	xhr.send();
}