import sqlite3
from datetime import datetime

# Conecta (ou cria) o banco de dados local
conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

# ======================================
# INSERIR DADOS NAS TABELAS EXISTENTES
# (as tabelas já foram criadas pelo seu colega)
# ======================================

# Inserir alunos
cursor.execute("INSERT INTO ALUNO (NOME, SEXO) VALUES (?, ?)", ("Lucas Almeida", "M"))
cursor.execute("INSERT INTO ALUNO (NOME, SEXO) VALUES (?, ?)", ("Maria Silva", "F"))

# Inserir autores
cursor.execute("INSERT INTO AUTOR (NOME) VALUES (?)", ("Machado de Assis",))
cursor.execute("INSERT INTO AUTOR (NOME) VALUES (?)", ("Clarice Lispector",))

# Inserir editoras
cursor.execute("INSERT INTO EDITORA (NOME) VALUES (?)", ("Companhia das Letras",))
cursor.execute("INSERT INTO EDITORA (NOME) VALUES (?)", ("Editora Record",))

# Inserir livros
cursor.execute("""
    INSERT INTO LIVRO (TIPO, TITULO, AREARELACIONADA, ANOPUBLICACAO, ISSN, ID_AUTOR, ID_EDITORA)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", ("F", "Dom Casmurro", "Literatura Brasileira", "1899-01-01", "1234-5678", 1, 1))

cursor.execute("""
    INSERT INTO LIVRO (TIPO, TITULO, AREARELACIONADA, ANOPUBLICACAO, ISSN, ID_AUTOR, ID_EDITORA)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", ("F", "A Hora da Estrela", "Ficção", "1977-01-01", "9876-5432", 2, 2))

# Inserir empréstimos
cursor.execute("""
    INSERT INTO EMPRESTIMO (ID_ALUNO, ID_LIVRO, DATAEMPRESTIMO, DATADEVOLUCAO)
    VALUES (?, ?, ?, ?)
""", (1, 1, datetime.now(), None))

cursor.execute("""
    INSERT INTO EMPRESTIMO (ID_ALUNO, ID_LIVRO, DATAEMPRESTIMO, DATADEVOLUCAO)
    VALUES (?, ?, ?, ?)
""", (2, 2, datetime.now(), datetime.now()))

# Confirmar alterações
conexao.commit()

print("✅ Dados inseridos com sucesso no SQLite!")

# Fechar conexão
cursor.close()
conexao.close()
