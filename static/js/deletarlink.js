function Deletar(pk) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", '/deletar-link?pk=' + pk);
	xhr.addEventListener("load", function() {
		window.location.reload();
	})
	xhr.send();
}