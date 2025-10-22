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
    turma =request.form.get('turma').split('-')
    turma = f"{turma[0]}º Ano{turma[1].upper()}"
    email = request.form.get('email')
    telefona = request.form.get('telefone')
    data = request.form.get('data')
    status = request.form.get('status')

    acao = request.form.get('acao')
    if acao == 'inserir':
        database.inserir_aluno(nome, matricula, turma, email, telefona, data, status)
        return  redirect('/alunos')
    elif acao == 'filtrar':
        return  redirect('/alunos')

# @bp.route('/alunos/<int:matricula>', methods=['GET'])
# def get_aluno(matricula):
#     conn = database.get_connection()
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM ALUNOS WHERE MATRICULA = ?', (matricula,))
#     colunas = [desc[0] for desc in cursor.description]
#     aluno = cursor.fetchone()
#     conn.close()
    
#     if aluno:
#         return jsonify(dict(zip(colunas, aluno)))
#     return jsonify({"error": "Aluno não encontrado"}), 404

# @bp.route('/alunos/<int:matricula>', methods=['PUT'])
# def edit_aluno(matricula):
#     data = request.get_json()
#     conn = database.get_connection()
#     cursor = conn.cursor()
#     cursor.execute('''
#         UPDATE ALUNOS
#         SET NOME = ?, TURMA = ?, EMAIL = ?, TELEFONE = ?, DATANASCIMENTO = ?, STATUS = ?
#         WHERE MATRICULA = ?
#     ''', (data['nome'], data['turma'], data['email'], data['telefone'], data['datanascimento'], data['status'], matricula))
    
#     conn.commit()
#     conn.close()
#     return jsonify({"message": "Aluno atualizado com sucesso!"})

@bp.route('/editar_aluno/<int:matricula>', methods=['POST'])
def editar_aluno(matricula):
    nome = request.form['nome']
    turma = request.form['turma']
    email = request.form['email']
    telefone = request.form['telefone']
    status = request.form['status']

    conn = database.get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE ALUNOS 
        SET NOME = ?, TURMA = ?, EMAIL = ?, TELEFONE = ?, STATUS = ?
        WHERE MATRICULA = ?
    """, (nome, turma, email, telefone, status, matricula))

    conn.commit()
    conn.close()

    return redirect('/alunos')
    
@bp.route('/emprestimos')
def emprestimos():
    alunos = database.get_alunos()
    livros = database.get_livros()
    emprestimos = database.get_emprestimos()

    return render_template('emprestimos.html', emprestimos=emprestimos,livros=livros, alunos=alunos)

@bp.route('/post_emprestimo', methods=['POST'])
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
@bp.route('/livros')
def livros():
    livros = database.get_livros()
    return render_template('livros.html', livros=livros)


@bp.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')






