create database suidio;
use suidio;

select * from obitos;

CREATE TABLE obitos (
    id_registro INT AUTO_INCREMENT PRIMARY KEY,
    `index_csv` VARCHAR(10), -- Captura a primeira coluna "" (índice)
    estado VARCHAR(2),
    ano INT,
    mes INT,
    DTOBITO DATE,
    DTNASC DATE,
    SEXO VARCHAR(20),
    RACACOR VARCHAR(20),
    ASSISTMED VARCHAR(20),
    ESCMAE VARCHAR(20),
    ESTCIV VARCHAR(20),
    ESC VARCHAR(20),
    OCUP VARCHAR(100),
    CODMUNRES VARCHAR(10),
    CAUSABAS VARCHAR(10),
    CAUSABAS_O VARCHAR(10),
    LOCOCOR VARCHAR(20),
    CIRURGIA VARCHAR(20)
);

-- Ativa a permissão de carregar arquivos locais nesta sessão
SET GLOBAL local_infile = 1;

LOAD DATA LOCAL INFILE 'C:/Users/Cleb/Downloads/suicidios_2010_a_2019.csv/suicidios.csv' -- Altere para o caminho onde o Suicidio está!!!!! 🗿🗿🗿🗿💀☠️💀☠️💀☠️💀☠️💀
INTO TABLE obitos
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(`index_csv`, estado, ano, mes, DTOBITO, DTNASC, SEXO, RACACOR, ASSISTMED, ESCMAE, ESTCIV, ESC, OCUP, CODMUNRES, CAUSABAS, CAUSABAS_O, LOCOCOR, CIRURGIA);

create view listar_obito as
SELECT 
    TIMESTAMPDIFF(YEAR, DTNASC, DTOBITO) AS idade, 
    SEXO, 
    estado 
FROM obitos;

create view registros_suicidios as
SELECT 
    estado, 
    COUNT(*) AS total_suicidios
FROM obitos
WHERE CAUSABAS REGEXP '^X(6[0-9]|7[0-9]|8[0-4])'
GROUP BY estado
ORDER BY total_suicidios DESC;

create view estados_afetados as
SELECT 
    estado, 
    COUNT(*) AS total_casos
FROM obitos
GROUP BY estado
ORDER BY total_casos DESC
LIMIT 10;

create view nivel_escolaridade as SELECT 
    ESC AS escolaridade, 
    COUNT(*) AS total_casos
FROM obitos
GROUP BY ESC
ORDER BY total_casos DESC;

create view registros_eciv as SELECT 
    ESTCIV AS estado_civil, 
    COUNT(*) AS total_casos
FROM obitos
GROUP BY ESTCIV
ORDER BY total_casos DESC;

create view media_estados as SELECT 
    estado, 
    ROUND(AVG(TIMESTAMPDIFF(YEAR, DTNASC, DTOBITO)), 1) AS media_idade
FROM obitos
WHERE DTNASC IS NOT NULL AND DTOBITO IS NOT NULL
GROUP BY estado
ORDER BY media_idade DESC;

create view casos as SELECT 
    estado, 
    ESTCIV AS estado_civil, 
    ESC AS escolaridade, 
    CAUSABAS AS causa_basica, 
    COUNT(*) AS quantidade_casos
FROM obitos
GROUP BY estado, ESTCIV, ESC, CAUSABAS
ORDER BY quantidade_casos DESC;

select * from obitos;
select * from listar_obito;
select * from registros_suicidios;
select * from estados_afetados;
select * from nivel_escolaridade;
select * from registros_eciv;
select * from media_estados;
