function Deletar(pk) {
    console.log('passeo')
    console.log('passeo')
    console.log('passeo')

	var deletarDocumentoXhr = new XMLHttpRequest();
	deletarDocumentoXhr.open("GET", '/documentos/deletar-nota-admin?pk=' + pk);
	deletarDocumentoXhr.addEventListener("load", function() {
		window.location.reload();
	})
	deletarDocumentoXhr.send();
}