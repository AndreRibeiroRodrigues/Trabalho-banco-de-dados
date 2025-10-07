from flask import Blueprint, render_template
import application.database as database
import sqlite3

bp = Blueprint('main', __name__)


@bp.route('/')
@bp.route('/apresentacao')
def index():
    return render_template('index.html')


@bp.route('/alunos')
def alunos():
    return render_template('alunos.html')

@bp.route('/emprestimos')
def emprestimos():
    return render_template('emprestimos.html')


@bp.route('/livros')
def livros():
    return render_template('livros.html')


@bp.route('/relatorios')
def relatorios():
    return render_template('relatorios.html')

@bp.route('/postalunos/', methods=['post'])
def postalunos():
    return render_template('postalunos.html')


