var selectSala = document.querySelector('#sala');
var selectHorario = document.querySelector('#horario');
var divHorario = document.querySelector('.div-horario');
var divBotao = document.querySelector('.div-botao');

selectSala.addEventListener("change", function() {
	var optionsHorario = document.querySelectorAll(".option-horario");
	divHorario.classList.remove('invisivel');
	divBotao.classList.add('invisivel');	
	optionsHorario.forEach(function(optionHorario) {
		if (optionHorario.classList.contains(selectSala.selectedIndex)) {
			optionHorario.classList.remove('invisivel');
			selectHorario.selectedIndex = 0;
		}
		else optionHorario.classList.add('invisivel');
	});
});

selectHorario.addEventListener("change", function() {
	var opcaoSelecionada = this.options[this.selectedIndex];
	if (opcaoSelecionada.classList.contains('btn-danger')) {
		selectHorario.selectedIndex = 0;
		alert('Esse horario já está reservado');
		divBotao.classList.add('invisivel');
	}
	else {
		divBotao.classList.remove('invisivel');
	}
})