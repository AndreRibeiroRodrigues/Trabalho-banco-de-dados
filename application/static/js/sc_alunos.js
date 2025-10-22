// function editarAluno(matricula) {
//         fetch(`/alunos/${matricula}`)
//             .then(res => res.json())
//             .then(aluno => {
//                 // Cria um formulário simples (ou pode abrir modal)
//                 const nome = prompt("Nome:", aluno.nome);
//                 const turma = prompt("Turma:", aluno.turma);
//                 const email = prompt("Email:", aluno.email);
//                 const telefone = prompt("Telefone:", aluno.telefone);
//                 const status = prompt("Status (ativo/inativo/pendente):", aluno.status);
    
//                 // Atualiza o aluno
//                 fetch(`/alunos/${matricula}`, {
//                     method: "PUT",
//                     headers: { "Content-Type": "application/json" },
//                     body: JSON.stringify({
//                         nome,
//                         turma,
//                         email,
//                         telefone,
//                         datanascimento: aluno.datanascimento,
//                         status
//                     })
//                 })
//                 .then(r => r.json())
//                 .then(resp => {
//                     alert(resp.message);
//                     location.reload(); // recarrega a página para ver a atualização
//                 });
//             });
//     }

function abrirModal(matricula, nome, turma, email, telefone, status) {
    document.getElementById("matricula").value = matricula;
    document.getElementById("nome").value = nome;
    document.getElementById("turma").value = turma;
    document.getElementById("email").value = email;
    document.getElementById("telefone").value = telefone;
    document.getElementById("status").value = status;

    document.getElementById("alunoModal").style.display = "block";
  }

  // Fecha o modal
function fecharModal() {
    document.getElementById("alunoModal").style.display = "none";
  }

  // Salva (exemplo)
  function salvarAluno() {
    const aluno = {
      matricula: document.getElementById("matricula").value,
      nome: document.getElementById("nome").value,
      turma: document.getElementById("turma").value,
      email: document.getElementById("email").value,
      telefone: document.getElementById("telefone").value,
      status: document.getElementById("status").value
    };

    console.log("Aluno atualizado:", aluno);
    alert("Dados salvos (simulação).");
    fecharModal();
  }

  // Fecha ao clicar fora
  window.onclick = function(event) {
    let modal = document.getElementById("alunoModal");
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }