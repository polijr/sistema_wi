function Deletar(pk) {
	var xhr = new XMLHttpRequest();
	xhr.open('GET', '/usuarios/deletar-organizador?pk=' + pk);
	xhr.addEventListener("load", function() {
	});
	xhr.send();
}