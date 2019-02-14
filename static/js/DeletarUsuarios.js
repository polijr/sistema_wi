function DeletarOrganizador(pk) {
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

function DeletarEmpresa(pk) {
	var xhr = new XMLHttpRequest();
	var conf = confirm("Deseja mesmo excluir esta empresa?")
	if (conf==true){
	xhr.open('GET', '/usuarios/deletar-empresa?pk=' + pk);
	xhr.addEventListener("load", function() {
	});
	xhr.send();
	location.reload();
	}
	else{
	    location.reload();
	}
}

function DeletarCaravaneiro(pk) {
	var xhr = new XMLHttpRequest();
	var conf = confirm("Deseja mesmo excluir este caravaneiro?")
	if (conf==true){
	xhr.open('GET', '/usuarios/deletar-caravaneiro?pk=' + pk);
	xhr.addEventListener("load", function() {
	});
	xhr.send();
	location.reload();
	}
	else{
	    location.reload();
	}
}