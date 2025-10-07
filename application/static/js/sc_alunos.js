        function cadastrarAluno() {
            const nome = document.getElementById('nome').value;
            const matricula = document.getElementById('matricula').value;
            const turma = document.getElementById('turma').value;
            const email = document.getElementById('email').value;
            const dataNascimento = document.getElementById('dataNascimento').value;
            const telefone = document.getElementById('telefone').value;
            const status = document.getElementById('status').value;

            // if (!nome || !matricula || !turma || !email) {
            //     alert('Por favor, preencha todos os campos obrigatórios (Nome, Matrícula, Turma e E-mail).');
            //     return;
            // }

            // alert('Aluno cadastrado com sucesso!\n\nNome: ' + nome + '\nMatrícula: ' + matricula);
            alert(dataNascimento);
            limparFiltros();
        }

        function buscarAlunos() {
            const nome = document.getElementById('nome').value.toLowerCase();
            const matricula = document.getElementById('matricula').value.toLowerCase();
            const turma = document.getElementById('turma').value;
            const status = document.getElementById('status').value;

            const linhas = document.querySelectorAll('#tabelaAlunos tbody tr');
            
            linhas.forEach(linha => {
                const nomeAluno = linha.cells[1].textContent.toLowerCase();
                const matriculaAluno = linha.cells[0].textContent.toLowerCase();
                const turmaAluno = linha.cells[2].textContent.toLowerCase();
                const statusAluno = linha.cells[6].textContent.toLowerCase();

                const matchNome = !nome || nomeAluno.includes(nome);
                const matchMatricula = !matricula || matriculaAluno.includes(matricula);
                const matchTurma = !turma || turmaAluno.includes(turma);
                const matchStatus = !status || statusAluno.includes(status);

                if (matchNome && matchMatricula && matchTurma && matchStatus) {
                    linha.style.display = '';
                } else {
                    linha.style.display = 'none';
                }
            });
        }

        function limparFiltros() {
            document.getElementById('nome').value = '';
            document.getElementById('matricula').value = '';
            document.getElementById('turma').value = '';
            document.getElementById('email').value = '';
            document.getElementById('telefone').value = '';
            document.getElementById('dataNascimento').value = '';
            document.getElementById('status').value = '';
            
            const linhas = document.querySelectorAll('#tabelaAlunos tbody tr');
            linhas.forEach(linha => linha.style.display = '');
        }

        function editarAluno(id) {
            alert('Editar aluno ID: ' + id);
        }

        function verHistorico(id) {
            alert('Visualizar histórico de empréstimos do aluno ID: ' + id);
        }