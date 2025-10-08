from flask import Blueprint, render_template, redirect, request
import application.database as database

bp = Blueprint('main', __name__)


@bp.route('/')
@bp.route('/apresentacao')
def index():
    return render_template('index.html')


@bp.route('/alunos')
def alunos():
    alunos = database.get_alunos()
    return render_template('alunos.html', alunos=alunos)

@bp.route('/emprestimos')
def emprestimos():
    alunos = database.get_alunos()
    livros = database.get_livros()
    emprestimos = database.get_emprestimos()
    return render_template('emprestimos.html', emprestimos=emprestimos,livros=livros, alunos=alunos)


@bp.route('/livros')
def livros():
    livros = database.get_livros()
    return render_template('livros.html', livros=livros)


@bp.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')

@bp.route('/post_aluno', methods=['POST']) # type: ignore
def post_aluno():
    nome = request.form.get('nome')
    matricula = request.form.get('matricula')
    turma =request.form.get('turma')
    email = request.form.get('email')
    telefona = request.form.get('telefone')
    data = request.form.get('data')
    status = request.form.get('status')

    acao = request.form.get('acao')
    if acao == 'inserir':
        
        return  redirect('/alunos')
    elif acao == 'filtrar':
        return


