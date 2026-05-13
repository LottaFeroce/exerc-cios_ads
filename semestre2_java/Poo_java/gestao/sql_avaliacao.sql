CREATE DATABASE Prova_calebica;
USE Prova_calebica;

CREATE TABLE Turmas (
    ID_turma INT AUTO_INCREMENT PRIMARY KEY,
    Nome_turma VARCHAR(45) NOT NULL,
    Semestre VARCHAR(45) NOT NULL
);

CREATE TABLE Alunos (
    ID_aluno INT AUTO_INCREMENT PRIMARY KEY,
    Nome_aluno VARCHAR(45) NOT NULL,
    Matricula VARCHAR(45) NOT NULL,
    Turmas_ID_turma INT NOT NULL,
    CONSTRAINT fk_aluno_turma FOREIGN KEY (Turmas_ID_turma) REFERENCES Turmas (ID_turma)
);

CREATE TABLE Avaliacoes (
    ID_avaliacoes INT AUTO_INCREMENT PRIMARY KEY,
    Peso INT NOT NULL,
    Turmas_ID_turma INT NOT NULL,
    CONSTRAINT fk_avaliacao_turma FOREIGN KEY (Turmas_ID_turma) REFERENCES Turmas (ID_turma)
);

CREATE TABLE Notas (
    ID_nota INT AUTO_INCREMENT PRIMARY KEY,
    Nota INT NOT NULL,
    Avaliacoes_ID_avaliacoes INT NOT NULL,
    Alunos_ID_aluno INT NOT NULL,
    CONSTRAINT fk_nota_avaliacao FOREIGN KEY (Avaliacoes_ID_avaliacoes) REFERENCES Avaliacoes (ID_avaliacoes),
    CONSTRAINT fk_nota_aluno FOREIGN KEY (Alunos_ID_aluno) REFERENCES Alunos (ID_aluno)
);
select * from turmas;
INSERT INTO Turmas (Nome_turma, Semestre)
VALUES
('ADS A', '1 Semestre'),
('Banco de Dados B', '2 Semestre');

INSERT INTO Alunos
(Nome_aluno, Matricula, Turmas_ID_turma)
VALUES
('Ana Silva', '2025001', 1),
('Carlos Souza', '2025002', 1),
('Juliana Lima', '2025003', 2);

INSERT INTO Avaliacoes
(Peso, Turmas_ID_turma)
VALUES
(10, 1),
(10, 1),
(10, 2);

INSERT INTO Notas
(Nota, Avaliacoes_ID_avaliacoes, Alunos_ID_aluno)
VALUES
(8, 1, 1),
(9, 2, 1),
(7, 1, 2),
(8, 2, 2),
(10, 3, 3);

SELECT 
    a.Nome_aluno, t.Nome_turma, AVG(n.Nota) AS Media_Final
FROM
    Notas n
        JOIN
    Alunos a ON n.Alunos_ID_aluno = a.ID_aluno
        JOIN
    Turmas t ON a.Turmas_ID_turma = t.ID_turma
GROUP BY a.ID_aluno;