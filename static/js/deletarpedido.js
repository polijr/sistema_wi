function Deletar(pk) {
	var deletarPedidoXhr = new XMLHttpRequest();
	deletarPedidoXhr.open('GET', '/pedidos/deletar-pedidos?pk=' + pk);
	deletarPedidoXhr.send();
}