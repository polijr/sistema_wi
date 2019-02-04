function Deletar(pk) {
	var xhr = new XMLHttpRequest();
	xhr.open('GET', '/pedidos/deletar_pedidos?pk=' + pk);
	xhr.send();
}