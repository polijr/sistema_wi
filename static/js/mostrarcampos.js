var selectSala = document.querySelector('#sala');
selectSala.addEventListener("change", function() {
	var divHorario = document.querySelector('.div-horario');
	divHorario.classList.remove('invisivel');
	var optionsHorario = document.querySelectorAll('.option-horario');
	optionsHorario.forEach(function(optionHorario) {
		if (optionHorario.classList.contains(selectSala.selectedIndex))
			optionHorario.classList.remove('invisivel');
		else optionHorario.classList.add('invisivel');
	});
});

var selectHorario = document.querySelector('#horario');
selectHorario.addEventListener("change", function() {
	var opcaoSelecionada = this.options[this.selectedIndex];
	if (opcaoSelecionada.classList.contains('btn-danger')) {
		opcaoSelecionada.removeAttr("selected");
		alert('Esse horario já está reservado');
	}
	else {
		var divBotao = document.querySelector('.div-botao');
		divBotao.classList.remove('invisivel');
	}
})