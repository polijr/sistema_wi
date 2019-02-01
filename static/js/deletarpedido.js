function Deletar(pk) {
	var xhr = new XMLHttpRequest();
	xhr.open('GET', '/pedidos/deletar-pedidos?pk=' + pk);
	xhr.addEventListener("load", function() {
	});
	xhr.send();
}