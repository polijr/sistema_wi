function Deletar(pk) {
	var deletarDocumentoXhr = new XMLHttpRequest();
	deletarDocumentoXhr.open("GET", '/documentos/deletar-nota?pk=' + pk);
	deletarDocumentoXhr.addEventListener("load", function() {
		window.location.reload();
	})
	deletarDocumentoXhr.send();
}