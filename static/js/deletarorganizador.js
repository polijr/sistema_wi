function Deletar(pk) {
	var xhr = new XMLHttpRequest();
	var conf = confirm("Deseja mesmo excluir este organizador?")
	if (conf==true){
	xhr.open('GET', '/usuarios/deletar-organizador?pk=' + pk);
	xhr.addEventListener("load", function() {
	});
	xhr.send();
	location.reload();
	}
	else{
	    location.reload();
	}
}