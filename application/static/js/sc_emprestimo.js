async function devolverEmprestimo(id) {
  if (!confirm("Tem certeza que deseja marcar este empréstimo como devolvido?")) return;

  try {
    const response = await fetch(`/emprestimos/devolver/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id: id }),

    });

    const result = await response.json();

    if (response.ok) {
      alert(result.message || "Livro devolvido com sucesso!");

      // Atualiza a linha visualmente (opcional)
      const linha = document.getElementById(`emprestimo-${id}`);
      if (linha) {
        linha.cells[6].textContent = "Devolvido";
      }
    } else {
      alert("Erro ao devolver: " + result.message);
    }
  } catch (erro) {
    console.error(erro);
    alert("Erro ao conectar com o servidor.");
  }
}