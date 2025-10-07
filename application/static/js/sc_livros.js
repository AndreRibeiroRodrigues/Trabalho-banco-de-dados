function adicionarLivro() {
    const titulo = document.getElementById('titulo').value;
    const autor = document.getElementById('autor').value;
    const isbn = document.getElementById('isbn').value;
    const categoria = document.getElementById('categoria').value;

    if (!titulo || !autor) {
        alert('Por favor, preencha pelo menos o título e o autor do livro.');
        return;
    }

    alert('Livro adicionado com sucesso!\n\nTítulo: ' + titulo + '\nAutor: ' + autor);
    limparFiltros();
}

function buscarLivros() {
    const titulo = document.getElementById('titulo').value.toLowerCase();
    const autor = document.getElementById('autor').value.toLowerCase();
    const isbn = document.getElementById('isbn').value.toLowerCase();
    const categoria = document.getElementById('categoria').value;

    const linhas = document.querySelectorAll('#tabelaLivros tbody tr');

    linhas.forEach(linha => {
        const tituloLivro = linha.cells[1].textContent.toLowerCase();
        const autorLivro = linha.cells[2].textContent.toLowerCase();
        const isbnLivro = linha.cells[3].textContent.toLowerCase();
        const categoriaLivro = linha.cells[4].textContent.toLowerCase();

        const matchTitulo = !titulo || tituloLivro.includes(titulo);
        const matchAutor = !autor || autorLivro.includes(autor);
        const matchIsbn = !isbn || isbnLivro.includes(isbn);
        const matchCategoria = !categoria || categoriaLivro.includes(categoria);

        if (matchTitulo && matchAutor && matchIsbn && matchCategoria) {
            linha.style.display = '';
        } else {
            linha.style.display = 'none';
        }
    });
}

function limparFiltros() {
    document.getElementById('titulo').value = '';
    document.getElementById('autor').value = '';
    document.getElementById('isbn').value = '';
    document.getElementById('categoria').value = '';

    const linhas = document.querySelectorAll('#tabelaLivros tbody tr');
    linhas.forEach(linha => linha.style.display = '');
}

function editarLivro(id) {
    alert('Editar livro ID: ' + id);
}

function excluirLivro(id) {
    if (confirm('Tem certeza que deseja excluir este livro?')) {
        alert('Livro ID ' + id + ' excluído com sucesso!');
    }
}