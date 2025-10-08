// function registrarEmprestimo() {
//     const aluno = document.getElementById('aluno').value;
//     const livro = document.getElementById('livro').value;
//     const dataEmprestimo = document.getElementById('dataEmprestimo').value;
//     const dataDevolucao = document.getElementById('dataDevolucao').value;

//     if (!aluno || !livro || !dataEmprestimo || !dataDevolucao) {
//         alert('Por favor, preencha todos os campos.');
//         return;
//     }

//     alert('Empréstimo registrado com sucesso!');
//     limparFiltros();
// }

// function devolverLivro(id) {
//     if (confirm('Confirmar devolução do livro?')) {
//         alert('Livro devolvido com sucesso! ID: ' + id);
//         location.reload();
//     }
// }

// function renovarEmprestimo(id) {
//     if (confirm('Renovar empréstimo por mais 14 dias?')) {
//         alert('Empréstimo renovado com sucesso! ID: ' + id);
//         location.reload();
//     }
// }

// function filtrarEmprestimos() {
//     alert('Filtro aplicado!');
// }

// function limparFiltros() {
//     document.getElementById('aluno').value = '';
//     document.getElementById('livro').value = '';
//     document.getElementById('dataEmprestimo').value = '';
//     document.getElementById('dataDevolucao').value = '';
// }

// // Set today's date as default
// const hoje = new Date().toISOString().split('T')[0];
// document.getElementById('dataEmprestimo').value = hoje;

// // Set default return date (14 days from today)
// const devolucao = new Date();
// devolucao.setDate(devolucao.getDate() + 14);
// document.getElementById('dataDevolucao').value = devolucao.toISOString().split('T')[0];