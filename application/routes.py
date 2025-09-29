from flask import Blueprint, render_template
import sqlite3

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/sobre')
def sobre():
    return '<h2>Página Sobre</h2><p>Esse site foi feito em Flask!</p>'