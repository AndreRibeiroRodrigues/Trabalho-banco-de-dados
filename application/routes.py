from flask import Blueprint, render_template, redirect, request, jsonify
import application.database as database

bp = Blueprint('main', __name__)


@bp.route('/')
@bp.route('/apresentacao')
def index():
    return render_template('index.html')

#aluno
@bp.route('/alunos')
def alunos():
    alunos = database.get_alunos()
    return render_template('alunos.html', alunos=alunos)

@bp.route('/post_aluno', methods=['POST']) # type: ignore
def post_aluno():
    nome = request.form.get('nome')
    matricula = request.form.get('matricula')
    turma =request.form.get('turma').split('-') # type: ignore
    turma = f"{turma[0]}º Ano{turma[1].upper()}"
    email = request.form.get('email')
    telefona = request.form.get('telefone')
    data = request.form.get('data')
    acao = request.form.get('acao')
    if acao == 'inserir':
        database.inserir_aluno(nome, matricula, turma, email, telefona, data)
        return  redirect('/alunos')
    elif acao == 'filtrar':
        return  redirect('/alunos')

@bp.route('/atualizar_aluno', methods=['POST'])
def atualizar_aluno():
    dados = request.get_json()

    matricula = dados['matricula']
    nome = dados['nome']
    turma = dados['turma']
    email = dados['email']
    telefone = dados['telefone']
    database.atualizarAluno(matricula, nome, turma, email, telefone)
    

    return jsonify({'mensagem': 'Aluno atualizado com sucesso!'})

@bp.route('/deletar_aluno', methods=['POST'])
def deletar_aluno():
    dados = request.get_json()
    matricula = dados['matricula']
    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM ALUNOS WHERE MATRICULA = ?', (matricula,))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Aluno deletado com sucesso!'})


#Emprestimo
@bp.route('/emprestimos')
def emprestimos():
    alunos = database.get_alunos()
    livros = database.get_livros()
    emprestimos = database.get_emprestimos()

    return render_template('emprestimos.html', emprestimos=emprestimos,livros=livros, alunos=alunos)

@bp.route('/emprestimos/adicionar', methods=['POST'])
def post_emprestimo():
    matricula = request.form.get('aluno')
    idlivro = request.form.get('livro')
    dataEmprestimo = request.form.get('dataEmprestimo')
    dataDevolucao = request.form.get('dataDevolucao')
    acao = request.form.get('acao')
    if acao == 'inserir':
        database.inserir_emprestimo(matricula, idlivro)
        return redirect('/emprestimos')
    else:
        return redirect('/emprestimos')

@bp.route('/emprestimos/devolver/<int:id>', methods=['PUT'])
def devolver_livro(id):
    database.devolver_livro(id)
    return jsonify({"message": "Livro devolvido com sucesso!"})
#livro
@bp.route('/livros')
def livros():
    livros = database.get_livros()
    return render_template('livros.html', livros=livros)

@bp.route('/post_livro', methods=['POST'])
def adicionar_livro():
    titulo = request.form.get('titulo')
    autor = request.form.get('autor')
    isbn = request.form.get('isbn')
    categoria = request.form.get('categoria')
    ano = request.form.get('ano')
    database.add_livro(titulo, autor, isbn, categoria, ano)
    return redirect('/livros')

@bp.route('/livros/editar/<int:id>', methods=['PUT'])
def editar_livro(id):
    dados = request.get_json()
    titulo = dados['titulo']
    autor = dados['autor']
    isbn = dados['isbn']
    categoria = dados['categoria']
    ano = dados['ano']
    database.atualizar_livro(id, titulo, autor, isbn, categoria, ano)
    return jsonify({"message": "Livro atualizado com sucesso!"})

@bp.route('/livros/excluir/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM LIVROS WHERE ID = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Livro excluído com sucesso!"})

@bp.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')






