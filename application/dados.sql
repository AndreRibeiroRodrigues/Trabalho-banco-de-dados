-- sera usado para popular o banco de dados inicialmente

-- =============================
-- AUTORES
-- =============================
INSERT INTO AUTOR (NOME) VALUES ('J. K. Rowling');            -- ID 1
INSERT INTO AUTOR (NOME) VALUES ('J. R. R. Tolkien');         -- ID 2
INSERT INTO AUTOR (NOME) VALUES ('George Orwell');            -- ID 3
INSERT INTO AUTOR (NOME) VALUES ('Machado de Assis');         -- ID 4
INSERT INTO AUTOR (NOME) VALUES ('Gabriel García Márquez');   -- ID 5
INSERT INTO AUTOR (NOME) VALUES ('Paulo Coelho');             -- ID 6
INSERT INTO AUTOR (NOME) VALUES ('Jane Austen');              -- ID 7
INSERT INTO AUTOR (NOME) VALUES ('Charlotte Brontë');         -- ID 8
INSERT INTO AUTOR (NOME) VALUES ('Emily Brontë');             -- ID 9
INSERT INTO AUTOR (NOME) VALUES ('Charles Dickens');          -- ID 10
INSERT INTO AUTOR (NOME) VALUES ('Fiódor Dostoiévski');       -- ID 11
INSERT INTO AUTOR (NOME) VALUES ('Liev Tolstói');             -- ID 12
INSERT INTO AUTOR (NOME) VALUES ('Gustave Flaubert');         -- ID 13
INSERT INTO AUTOR (NOME) VALUES ('Oscar Wilde');              -- ID 14
INSERT INTO AUTOR (NOME) VALUES ('Antoine de Saint-Exupéry'); -- ID 15
INSERT INTO AUTOR (NOME) VALUES ('Dan Brown');                -- ID 16
INSERT INTO AUTOR (NOME) VALUES ('Suzanne Collins');          -- ID 17
INSERT INTO AUTOR (NOME) VALUES ('Patrick Rothfuss');         -- ID 18
INSERT INTO AUTOR (NOME) VALUES ('C. S. Lewis');              -- ID 19
INSERT INTO AUTOR (NOME) VALUES ('Markus Zusak');             -- ID 20
INSERT INTO AUTOR (NOME) VALUES ('Khaled Hosseini');          -- ID 21

-- =============================
-- EDITORAS
-- =============================
INSERT INTO EDITORA (NOME) VALUES ('Bloomsbury Publishing');       -- ID 1
INSERT INTO EDITORA (NOME) VALUES ('Allen & Unwin');               -- ID 2
INSERT INTO EDITORA (NOME) VALUES ('Secker & Warburg');            -- ID 3
INSERT INTO EDITORA (NOME) VALUES ('Companhia das Letras');        -- ID 4
INSERT INTO EDITORA (NOME) VALUES ('Editorial Sudamericana');      -- ID 5
INSERT INTO EDITORA (NOME) VALUES ('HarperCollins');               -- ID 6
INSERT INTO EDITORA (NOME) VALUES ('Penguin Books');               -- ID 7
INSERT INTO EDITORA (NOME) VALUES ('Chapman & Hall');              -- ID 8
INSERT INTO EDITORA (NOME) VALUES ('Gallimard');                   -- ID 9
INSERT INTO EDITORA (NOME) VALUES ('Random House');                -- ID 10

-- =============================
-- LIVROS (50 registros)
-- =============================

-- Rowling
INSERT INTO LIVRO VALUES ('F', 'Harry Potter e a Pedra Filosofal', 'Fantasia', '1997-06-26', '1000-0001', 1, 1);
INSERT INTO LIVRO VALUES ('F', 'Harry Potter e a Câmara Secreta', 'Fantasia', '1998-07-02', '1000-0002', 1, 1);
INSERT INTO LIVRO VALUES ('F', 'Harry Potter e o Prisioneiro de Azkaban', 'Fantasia', '1999-07-08', '1000-0003', 1, 1);
INSERT INTO LIVRO VALUES ('F', 'Harry Potter e o Cálice de Fogo', 'Fantasia', '2000-07-08', '1000-0004', 1, 1);

-- Tolkien
INSERT INTO LIVRO VALUES ('F', 'O Senhor dos Anéis: A Sociedade do Anel', 'Fantasia', '1954-07-29', '1000-0005', 2, 2);
INSERT INTO LIVRO VALUES ('F', 'O Senhor dos Anéis: As Duas Torres', 'Fantasia', '1954-11-11', '1000-0006', 2, 2);
INSERT INTO LIVRO VALUES ('F', 'O Senhor dos Anéis: O Retorno do Rei', 'Fantasia', '1955-10-20', '1000-0007', 2, 2);
INSERT INTO LIVRO VALUES ('F', 'O Hobbit', 'Fantasia', '1937-09-21', '1000-0008', 2, 2);

-- Orwell
INSERT INTO LIVRO VALUES ('D', '1984', 'Distopia', '1949-06-08', '1000-0009', 3, 3);
INSERT INTO LIVRO VALUES ('S', 'A Revolução dos Bichos', 'Sátira Política', '1945-08-17', '1000-0010', 3, 3);

-- Machado de Assis
INSERT INTO LIVRO VALUES ('R', 'Dom Casmurro', 'Literatura Brasileira', '1899-01-01', '1000-0011', 4, 4);
INSERT INTO LIVRO VALUES ('R', 'Memórias Póstumas de Brás Cubas', 'Literatura Brasileira', '1881-01-01', '1000-0012', 4, 4);

-- García Márquez
INSERT INTO LIVRO VALUES ('R', 'Cem Anos de Solidão', 'Realismo Mágico', '1967-05-30', '1000-0013', 5, 5);
INSERT INTO LIVRO VALUES ('R', 'O Amor nos Tempos do Cólera', 'Romance', '1985-01-01', '1000-0014', 5, 5);

-- Paulo Coelho
INSERT INTO LIVRO VALUES ('R', 'O Alquimista', 'Ficção Filosófica', '1988-01-01', '1000-0015', 6, 4);
INSERT INTO LIVRO VALUES ('R', 'Brida', 'Ficção Filosófica', '1990-01-01', '1000-0016', 6, 4);

-- Austen
INSERT INTO LIVRO VALUES ('R', 'Orgulho e Preconceito', 'Romance', '1813-01-28', '1000-0017', 7, 7);
INSERT INTO LIVRO VALUES ('R', 'Razão e Sensibilidade', 'Romance', '1811-10-30', '1000-0018', 7, 7);

-- Brontës
INSERT INTO LIVRO VALUES ('R', 'Jane Eyre', 'Romance', '1847-10-16', '1000-0019', 8, 7);
INSERT INTO LIVRO VALUES ('R', 'O Morro dos Ventos Uivantes', 'Romance', '1847-12-01', '1000-0020', 9, 7);

-- Dickens
INSERT INTO LIVRO VALUES ('R', 'Oliver Twist', 'Romance', '1838-01-01', '1000-0021', 10, 8);
INSERT INTO LIVRO VALUES ('R', 'Um Conto de Natal', 'Ficção Clássica', '1843-12-19', '1000-0022', 10, 8);

-- Dostoiévski
INSERT INTO LIVRO VALUES ('R', 'Crime e Castigo', 'Romance Psicológico', '1866-01-01', '1000-0023', 11, 7);
INSERT INTO LIVRO VALUES ('R', 'Os Irmãos Karamázov', 'Romance Filosófico', '1880-01-01', '1000-0024', 11, 7);

-- Tolstói
INSERT INTO LIVRO VALUES ('R', 'Guerra e Paz', 'Romance Histórico', '1869-01-01', '1000-0025', 12, 9);
INSERT INTO LIVRO VALUES ('R', 'Anna Kariênina', 'Romance', '1877-01-01', '1000-0026', 12, 9);

-- Flaubert
INSERT INTO LIVRO VALUES ('R', 'Madame Bovary', 'Romance', '1857-01-01', '1000-0027', 13, 9);

-- Wilde
INSERT INTO LIVRO VALUES ('R', 'O Retrato de Dorian Gray', 'Romance', '1890-01-01', '1000-0028', 14, 7);

-- Exupéry
INSERT INTO LIVRO VALUES ('I', 'O Pequeno Príncipe', 'Infantil/Filosofia', '1943-04-06', '1000-0029', 15, 10);

-- Dan Brown
INSERT INTO LIVRO VALUES ('T', 'O Código Da Vinci', 'Thriller', '2003-01-01', '1000-0030', 16, 6);
INSERT INTO LIVRO VALUES ('T', 'Anjos e Demônios', 'Thriller', '2000-01-01', '1000-0031', 16, 6);

-- Collins
INSERT INTO LIVRO VALUES ('D', 'Jogos Vorazes', 'Distopia', '2008-01-01', '1000-0032', 17, 6);
INSERT INTO LIVRO VALUES ('D', 'Em Chamas', 'Distopia', '2009-01-01', '1000-0033', 17, 6);
INSERT INTO LIVRO VALUES ('D', 'A Esperança', 'Distopia', '2010-01-01', '1000-0034', 17, 6);

-- Rothfuss
INSERT INTO LIVRO VALUES ('F', 'O Nome do Vento', 'Fantasia', '2007-01-01', '1000-0035', 18, 10);
INSERT INTO LIVRO VALUES ('F', 'O Temor do Sábio', 'Fantasia', '2011-01-01', '1000-0036', 18, 10);

-- Lewis
INSERT INTO LIVRO VALUES ('F', 'O Leão, a Feiticeira e o Guarda-Roupa', 'Fantasia', '1950-10-16', '1000-0037', 19, 6);
INSERT INTO LIVRO VALUES ('F', 'Príncipe Caspian', 'Fantasia', '1951-01-01', '1000-0038', 19, 6);

-- Zusak
INSERT INTO LIVRO VALUES ('R', 'A Menina que Roubava Livros', 'Ficção Histórica', '2005-01-01', '1000-0039', 20, 10);

-- Hosseini
INSERT INTO LIVRO VALUES ('R', 'O Caçador de Pipas', 'Romance', '2003-01-01', '1000-0040', 21, 10);
INSERT INTO LIVRO VALUES ('R', 'A Cidade do Sol', 'Romance', '2007-01-01', '1000-0041', 21, 10);

-- + extra para completar 50 livros
INSERT INTO LIVRO VALUES ('R', 'Persuasão', 'Romance', '1817-01-01', '1000-0042', 7, 7);
INSERT INTO LIVRO VALUES ('R', 'Grandes Esperanças', 'Romance', '1861-01-01', '1000-0043', 10, 8);
INSERT INTO LIVRO VALUES ('R', 'O Idiota', 'Romance Psicológico', '1869-01-01', '1000-0044', 11, 7);
INSERT INTO LIVRO VALUES ('R', 'Ressurreição', 'Romance Filosófico', '1899-01-01', '1000-0045', 12, 9);
INSERT INTO LIVRO VALUES ('R', 'Educação Sentimental', 'Romance', '1869-01-01', '1000-0046', 13, 9);
INSERT INTO LIVRO VALUES ('R', 'De Profundis', 'Filosofia', '1905-01-01', '1000-0047', 14, 7);
INSERT INTO LIVRO VALUES ('I', 'Carta a um Refém', 'Filosofia', '1944-01-01', '1000-0048', 15, 10);
INSERT INTO LIVRO VALUES ('T', 'O Símbolo Perdido', 'Thriller', '2009-01-01', '1000-0049', 16, 6);
INSERT INTO LIVRO VALUES ('D', 'Contos da Fome', 'Distopia', '2012-01-01', '1000-0050', 17, 6);
