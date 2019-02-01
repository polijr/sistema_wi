function Deletar(pk) {
	var xhr = new XMLHttpRequest();
	xhr.open('GET', '/pedidos/deletar_pedidos?pk=' + pk);
	xhr.addEventListener("load", function() {
		if (this.status = 200)
			alert('oi');
	});
	xhr.send();
}