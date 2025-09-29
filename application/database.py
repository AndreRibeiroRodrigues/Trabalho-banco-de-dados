import sqlite3


def get_db_connection():
    conn = sqlite3.connect('banco_de_dados.db')
    conn.row_factory = sqlite3.Row
    return conn

#Chame a funcão get_db_connection() para obter uma conexão com o banco de dados SQLite.
# Exemplo de uso:
# conn = get_db_connection()
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM tabela')
# rows = cursor.fetchall()
# conn.close()
# Lembre-se de fechar a conexão quando terminar.