import sqlite3
import os


def get_db_connection():
    conn = sqlite3.connect('banco_de_dados.db')
    conn.row_factory = sqlite3.Row
    return conn


# Chame a funcão get_db_connection() para obter uma conexão com o banco de dados SQLite.
# Exemplo de uso:
# conn = get_db_connection()
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM tabela')
# rows = cursor.fetchall()
# conn.close()
# Lembre-se de fechar a conexão quando terminar.

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    base_dir = os.path.dirname(__file__)
    schema_path = os.path.join(base_dir, 'schema.sql')
    with open(schema_path) as f:
        schema = f.read()
    cursor.executescript(schema)
    conn.commit()
    conn.close()


# A função init_db() inicializa o banco de dados executando um script SQL a partir de um arquivo chamado schema.sql.
# Certifique-se de ter um arquivo schema.sql no mesmo diretório com a estrutura do banco

def get_contagem_tabelas():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM ALUNO;")
    alunos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM EMPRESTIMO;")
    emprestimos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM LIVRO;")
    livros = cursor.fetchone()[0]
    print(alunos, emprestimos, livros)
    return alunos, emprestimos, livros
    # Exemplo de uso:
    # init_db()
    conn.close()
