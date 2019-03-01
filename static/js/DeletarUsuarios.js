function DeletarOrganizador(pk) {
	var deletarOrganizadorXhr = new XMLHttpRequest();
	var conf = confirm("Deseja mesmo excluir este organizador?")
	if (conf==true){
	deletarOrganizadorXhr.open('GET', '/usuarios/deletar-organizador?pk=' + pk);
	deletarOrganizadorXhr.addEventListener("load", function() {
	});
	deletarOrganizadorXhr.send();
	}
    location.reload();
}

function DeletarEmpresa(pk) {
	var deletarEmpresaXhr = new XMLHttpRequest();
	var conf = confirm("Deseja mesmo excluir esta empresa?")
	if (conf==true){
	deletarEmpresaXhr.open('GET', '/usuarios/deletar-empresa?pk=' + pk);
	deletarEmpresaXhr.addEventListener("load", function() {
	});
	deletarEmpresaXhr.send();
	}
	location.reload();
}

function DeletarCaravaneiro(pk) {
	var deletarCaravaneiroXhr = new XMLHttpRequest();
	var conf = confirm("Deseja mesmo excluir este caravaneiro?")
	if (conf==true){
	deletarCaravaneiroXhr.open('GET', '/usuarios/deletar-caravaneiro?pk=' + pk);
	deletarCaravaneiroXhr.addEventListener("load", function() {
	});
	deletarCaravaneiroXhr.send();
	}
    location.reload();
}

function DeletarOrganizadores(){
    var deletarOrganizadoresXhr = new XMLHttpRequest();
	var conf = confirm("Deseja mesmo excluir todos organizadores?")
	if (conf==true){
	    deletarOrganizadoresXhr.open('GET', '/usuarios/deletar-organizadores');
	    deletarOrganizadoresXhr.addEventListener("load", function() {
	});
	deletarOrganizadoresXhr.send();
	}
    location.reload();
}

function DeletarEmpresas(){
    var deletarEmpresasXhr = new XMLHttpRequest();
	var conf = confirm("Deseja mesmo excluir todas empresas?")
	if (conf==true){
	    deletarEmpresasXhr.open('GET', '/usuarios/deletar-empresas');
	    deletarEmpresasXhr.addEventListener("load", function() {
	});
	deletarEmpresasXhr.send();
	}
    location.reload();
}

function DeletarCaravaneiros(){
    var deletarCaravaneirosXhr = new XMLHttpRequest();
	var conf = confirm("Deseja mesmo excluir todos caravaneiros?")
	if (conf==true){
	    deletarCaravaneirosXhr.open('GET', '/usuarios/deletar-caravaneiros');
	    deletarCaravaneirosXhr.addEventListener("load", function() {
	});
	deletarCaravaneirosXhr.send();
	}
    location.reload();
}