import sqlite3
import os
import datetime


def get_connection():
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
    conn = get_connection()
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

def inserir_dados():
    conn = get_connection()
    cursor = conn.cursor()
    base_dir = os.path.dirname(__file__)
    schema_path = os.path.join(base_dir, 'dados.sql')
    with open(schema_path) as f:
        schema = f.read()
    cursor.executescript(schema)
    conn.commit()
    conn.close()

#função para pegar os alunos do banco de dados
def get_alunos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM  ALUNOS')
    alunos = cursor.fetchall()
    conn.close()
    return alunos

def get_livros():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM LIVROS')
    livros = cursor.fetchall()
    conn.close()
    return livros

def get_emprestimos():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT 
            e.ID AS id_emprestimo,
            a.NOME AS Aluno,
            l.TITULO AS Livro,
            e.DATAEMPRESTIMO,
            e.DATADEVOLUCAO,
            e.STATUS
        FROM EMPRESTIMOS e
        JOIN ALUNOS a ON e.ID_ALUNO = a.MATRICULA
        JOIN LIVROS l ON e.ID_LIVRO = l.ID;
    ''')
    
    # # Pegar o nome das colunas
    # colunas = [desc[0] for desc in cursor.description]
    # # Converter o resultado em lista de dicionários
    # emprestimos = [dict(zip(colunas, linha)) for linha in cursor.fetchall()]
    emprestimos = cursor.fetchall()
    conn.close()
    return emprestimos

def inserir_aluno(nome, matricula, turma, email, telefone, data, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ALUNOS (NOME, MATRICULA, TURMA, EMAIL, TELEFONE, DATANASCIMENTO, STATUS) VALUES (?, ?, ?, ?, ?, ?, ?)',
                   (nome, matricula, turma, email, telefone, data, status))
    conn.commit()
    conn.close

def inserir_emprestimo(matricula, idlivro):
    dataEmprestimo = datetime.datetime.now().strftime('%Y-%m-%d')
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO EMPRESTIMOS (ID_ALUNO, ID_LIVRO, DATAEMPRESTIMO) VALUES (?, ?, ?)',
                    (matricula, idlivro, dataEmprestimo))
    conn.commit()
    conn.close()
