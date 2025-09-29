from flask import Blueprint, render_template
import application.database as database
import sqlite3

bp = Blueprint('main', __name__)


@bp.route('/')
@bp.route('/apresentacao')
def index():
    alunos, emprestimos, livros = database.get_contagem_tabelas()
    return render_template('index.html', alunos=alunos, emprestimos=emprestimos, livros=livros)


@bp.route('/paginaInicial')
def paginaInicial():
    return render_template('paginaInicial.html')


@bp.route('/sobre')
def sobre():
    return '<h2>Página Sobre</h2><p>Esse site foi feito em Flask!</p>'
