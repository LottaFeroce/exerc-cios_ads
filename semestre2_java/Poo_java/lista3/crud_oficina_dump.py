"""CREATE DATABASE oficina;
USE oficina;
select * from funcionarios;

CREATE TABLE funcionarios (
    id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cargo VARCHAR(50),
    salario DECIMAL(10,2)
);

CREATE TABLE proprietarios (
    id_proprietario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(15)
);

CREATE TABLE carros (
    id_carro INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100),
    placa VARCHAR(10),
    id_proprietario INT,
    FOREIGN KEY (id_proprietario) REFERENCES proprietarios(id_proprietario)
);
"""