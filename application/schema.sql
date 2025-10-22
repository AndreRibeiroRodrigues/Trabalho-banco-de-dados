--DELETA AS TABELAS CASO EXISTAM
DROP TABLE IF EXISTS EMPRESTIMO;
DROP TABLE IF EXISTS ALUNO;
DROP TABLE IF EXISTS LIVRO;

CREATE TABLE IF NOT EXISTS ALUNOS (
    MATRICULA INTEGER PRIMARY KEY,
    NOME TEXT NOT NULL,
    TURMA TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    TELEFONE TEXT NOT NULL,
    DATANASCIMENTO DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS LIVROS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    TITULO TEXT NOT NULL,   
    AUTOR TEXT NOT NULL,
    ISBN TEXT NOT NULL,
    CATEGORIA TEXT NOT NULL,
    ANO INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS EMPRESTIMOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_ALUNO INTEGER NOT NULL,
    ID_LIVRO INTEGER NOT NULL,
    DATAEMPRESTIMO DATE NOT NULL,
    DATADEVOLUCAO TIMESTAMP,
    STATUS TEXT ,
    FOREIGN KEY (ID_ALUNO) REFERENCES ALUNO(MATRICULA),
    FOREIGN KEY (ID_LIVRO) REFERENCES LIVRO(ID)
);

INSERT INTO LIVROS (TITULO, AUTOR, ISBN, CATEGORIA, ANO) VALUES
('Dom Quixote', 'Miguel de Cervantes', '9788491050297', 'Romance', 1605),
('Cem Anos de Solidão', 'Gabriel García Márquez', '9788535933861', 'Ficção', 1967),
('1984', 'George Orwell', '9780451524935', 'Distopia', 1949),
('A Revolução dos Bichos', 'George Orwell', '9788535914846', 'Sátira política', 1945),
('O Senhor dos Anéis', 'J.R.R. Tolkien', '9788578277109', 'Fantasia', 1954),
('O Hobbit', 'J.R.R. Tolkien', '9780007458424', 'Fantasia', 1937),
('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', '9788532530780', 'Fantasia', 1997),
('Harry Potter e o Prisioneiro de Azkaban', 'J.K. Rowling', '9788532530810', 'Fantasia', 1999),
('A Menina que Roubava Livros', 'Markus Zusak', '9788579800245', 'Drama', 2005),
('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', '9788522031459', 'Infantil', 1943),
('O Código Da Vinci', 'Dan Brown', '9788575421468', 'Suspense', 2003),
('Anjos e Demônios', 'Dan Brown', '9788575421475', 'Suspense', 2000),
('Inferno', 'Dan Brown', '9788535922680', 'Suspense', 2013),
('Orgulho e Preconceito', 'Jane Austen', '9788537812835', 'Romance', 1813),
('Emma', 'Jane Austen', '9780141439587', 'Romance', 1815),
('Frankenstein', 'Mary Shelley', '9780143131847', 'Terror', 1818),
('Drácula', 'Bram Stoker', '9788551002288', 'Terror', 1897),
('O Morro dos Ventos Uivantes', 'Emily Brontë', '9788556510672', 'Romance', 1847),
('O Apanhador no Campo de Centeio', 'J.D. Salinger', '9780316769488', 'Ficção', 1951),
('Moby Dick', 'Herman Melville', '9780142437247', 'Aventura', 1851),
('A Divina Comédia', 'Dante Alighieri', '9788572326971', 'Poesia', 1320),
('O Conde de Monte Cristo', 'Alexandre Dumas', '9788579027048', 'Aventura', 1844),
('Os Três Mosqueteiros', 'Alexandre Dumas', '9788579027055', 'Aventura', 1844),
('Crime e Castigo', 'Fiódor Dostoiévski', '9788537809989', 'Romance psicológico', 1866),
('Os Irmãos Karamázov', 'Fiódor Dostoiévski', '9788535932146', 'Romance filosófico', 1880),
('Guerra e Paz', 'Liev Tolstói', '9788572326971', 'Romance histórico', 1869),
('Anna Kariênina', 'Liev Tolstói', '9788535918126', 'Romance', 1877),
('O Nome da Rosa', 'Umberto Eco', '9788535910472', 'Mistério', 1980),
('O Alquimista', 'Paulo Coelho', '9788575427583', 'Ficção espiritual', 1988),
('Brida', 'Paulo Coelho', '9788576651017', 'Espiritualidade', 1990),
('Veronika Decide Morrer', 'Paulo Coelho', '9788532512068', 'Drama', 1998),
('It: A Coisa', 'Stephen King', '9788560280940', 'Terror', 1986),
('O Iluminado', 'Stephen King', '9788599296492', 'Terror', 1977),
('Sob a Redoma', 'Stephen King', '9788580411711', 'Suspense', 2009),
('O Conto da Aia', 'Margaret Atwood', '9788532520667', 'Distopia', 1985),
('O Sol é Para Todos', 'Harper Lee', '9788525052246', 'Drama social', 1960),
('As Crônicas de Nárnia', 'C.S. Lewis', '9788578277109', 'Fantasia', 1950),
('Percy Jackson e o Ladrão de Raios', 'Rick Riordan', '9788580575390', 'Fantasia', 2005),
('A Maldição do Titã', 'Rick Riordan', '9788580575406', 'Fantasia', 2007),
('Jogos Vorazes', 'Suzanne Collins', '9788579800245', 'Distopia', 2008),
('Em Chamas', 'Suzanne Collins', '9788579800252', 'Distopia', 2009),
('A Esperança', 'Suzanne Collins', '9788579800269', 'Distopia', 2010),
('A Culpa é das Estrelas', 'John Green', '9788565765626', 'Romance', 2012),
('Cidades de Papel', 'John Green', '9788580573747', 'Juvenil', 2008),
('Tartarugas Até Lá Embaixo', 'John Green', '9788551002936', 'Juvenil', 2017),
('O Velho e o Mar', 'Ernest Hemingway', '9788573264722', 'Literatura clássica', 1952),
('Por Quem os Sinos Dobram', 'Ernest Hemingway', '9788537812569', 'Romance histórico', 1940),
('O Retrato de Dorian Gray', 'Oscar Wilde', '9788537812620', 'Romance filosófico', 1890),
('A Metamorfose', 'Franz Kafka', '9788537812552', 'Ficção existencial', 1915),
('O Processo', 'Franz Kafka', '9788535932139', 'Ficção filosófica', 1925);
